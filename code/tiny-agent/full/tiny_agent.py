# tiny_agent.py, full: every Appendix D checkpoint
# applied. Compare it with your own version.
# Runs offline. The "model" is a stand-in you can
# swap for a real one later (see Appendix D).
import json
import re

# ---- 1. Data the tools can reach ----------------
CATALOG = {
    "ECH-800": {"name": "Echo Studio Mic",
                "price": 129, "stock": 0},
    "PLS-400": {"name": "Pulse Earbuds",
                "price": 79, "stock": 120},
}
ORDERS = {
    "ORD-9001": {"customer": "alex", "total": 79,
                 "sku": "PLS-400", "days_ago": 5},
    "ORD-9003": {"customer": "sam", "total": 129,
                 "sku": "ECH-800", "days_ago": 45},
    "ORD-9004": {"customer": "lee", "total": 400,
                 "sku": "VLT-700", "days_ago": 3},
    "ORD-9006": {"customer": "alex", "total": 19,
                 "sku": "CBL-100", "days_ago": 2},
}
FINAL_SALE = {"CBL-100"}  # clearance: no refunds
POLICY = [
    "Refunds are allowed within 30 days.",
    "Refunds over $150 need a person to approve.",
    "Orders ship within 2 business days.",
    "Returns need the original box.",
]
TOP_K = 1  # how many passages reach the model
REFUND_DAYS = 30    # refund window
REFUND_LIMIT = 150  # dollars; above this, a person
                    # must approve

# ---- 2. Tools: ordinary functions ----------------
def get_product(sku):
    item = CATALOG.get(sku)
    if item is None:
        return {"error": f"no product {sku}"}
    return {"sku": sku, **item}

def get_order(order_id, user):
    order = ORDERS.get(order_id)
    if order is None:
        return {"error": f"no order {order_id}"}
    # Permission check: users see only their orders.
    if order["customer"] != user:
        return {"error": "that isn't your order"}
    return {"order_id": order_id, **order}

def refund(order_id, user):
    order = get_order(order_id, user)
    if "error" in order:
        return order
    # Guardrails: enforced in code, every time.
    if order["sku"] in FINAL_SALE:
        return {"error": "final-sale items can't "
                "be refunded"}
    if order["days_ago"] > REFUND_DAYS:
        return {"error": "past the 30-day window"}
    if order["total"] > REFUND_LIMIT:
        return {"refund": "sent_for_approval",
                "amount": order["total"]}
    return {"refund": "done", "amount": order["total"]}

def words(text):
    return set(text.lower().strip("?.").split())

def search_policy(query):
    q = words(query)
    ranked = sorted(POLICY, reverse=True,
                    key=lambda p: len(q & words(p)))
    return {"passages": ranked[:TOP_K]}

CARRIER_UP = True  # set False to test an outage

def get_shipping(order_id, user):
    order = get_order(order_id, user)
    if "error" in order:
        return order
    if not CARRIER_UP:
        return {"error": "the carrier isn't "
                "answering, try again later"}
    return {"order_id": order_id,
            "carrier": "ParcelCo", "eta_days": 2}

TOOLS = {"get_product": get_product,
         "get_order": get_order,
         "refund": refund,
         "search_policy": search_policy,
         "get_shipping": get_shipping}
NEEDS_USER = {"get_order", "refund",
              "get_shipping"}  # who asks

# ---- 3. The model (a fake one, for now) ----------
SKU = re.compile(r"[A-Z]{3}-[0-9]{3}")  # ECH-800

def fake_model(messages):
    """Reads the conversation and returns either a
    tool request or a final answer, as a real model
    would. Simple rules stand in for prediction."""
    last = messages[-1]
    if last["role"] == "tool":
        return answer_from(json.loads(last["content"]))
    if "policy" in last["content"].lower():
        return {"tool": "search_policy",
                "args": {"query": last["content"]}}
    words = last["content"].replace("?", " ").split()
    for w in words:
        if SKU.fullmatch(w):  # any SKU, real or not
            return {"tool": "get_product",
                    "args": {"sku": w}}
        if w.startswith("ORD-"):
            if "ship" in last["content"].lower():
                return {"tool": "get_shipping",
                        "args": {"order_id": w}}
            if "refund" in last["content"].lower():
                return {"tool": "refund",
                        "args": {"order_id": w}}
            return {"tool": "get_order",
                    "args": {"order_id": w}}
    return {"answer": "I can help with products "
            "and orders. What do you need?"}

def answer_from(data):
    if "error" in data:
        return {"answer": "Sorry, I can't do that: "
                + data["error"] + "."}
    if "passages" in data:
        return {"answer": " ".join(data["passages"])}
    if "carrier" in data:
        return {"answer": f"It ships with "
                f"{data['carrier']} and should arrive "
                f"in {data['eta_days']} days."}
    if data.get("refund") == "done":
        return {"answer": "Done. I've refunded "
                f"${data['amount']}."}
    if data.get("refund") == "sent_for_approval":
        return {"answer": "A refund that size needs "
                "a person to approve it. I've sent "
                "it to the team."}
    if "stock" in data:
        stock = ("in stock" if data["stock"] > 0
                 else "out of stock")
        return {"answer": f"The {data['name']} costs "
                f"${data['price']} and is {stock}."}
    return {"answer": f"Order {data['order_id']} "
            f"was placed {data['days_ago']} days ago."}

# ---- 4. The harness: the loop around the model ---
SYSTEM = ("You are ShopBot. Answer only from tool "
          "results. Never guess prices.")
TRACE = []  # every tool call, for tests to check

NOTES = {}  # one saved note per user

def run_turn(question, user, model=fake_model):
    if "prefer" in question.lower():
        NOTES[user] = question  # newest wins
    note = NOTES.get(user, "none")
    print(f"  [trace] memory {note!r}")
    system = SYSTEM + f" Note on this user: {note}"
    messages = [{"role": "system", "content": system},
                {"role": "user", "content": question}]
    for step in range(5):  # stop runaway loops
        size = sum(len(m["content"])
                   for m in messages)
        print(f"  [trace] about {size // 4} tokens in")
        reply = model(messages)
        if "answer" in reply:
            print(f"  [trace] answer after {step} "
                  "tool call(s)")
            return reply["answer"]
        name, args = reply["tool"], reply["args"]
        print(f"  [trace] tool {name} {args}")
        args.pop("user", None)  # the model can't pick
        if name not in TOOLS:
            result = {"error": f"unknown tool {name}"}
        elif name in NEEDS_USER:
            result = TOOLS[name](user=user, **args)
        else:
            result = TOOLS[name](**args)
        print(f"  [trace] result {result}")
        TRACE.append((name, args, result))
        messages.append({"role": "assistant",
                         "content": json.dumps(reply)})
        messages.append({"role": "tool",
                         "content": json.dumps(result)})
    return "Sorry, I got stuck. A person will help."

def rogue(messages):
    """A stand-in model that tries to act as Lee."""
    last = messages[-1]
    if last["role"] == "tool":
        data = json.loads(last["content"])
        return answer_from(data)
    return {"tool": "refund",
            "args": {"order_id": "ORD-9004",
                     "user": "lee"}}

# ---- 5. Try it ----------------------------------
if __name__ == "__main__":
    tests = [
        ("alex", "Is ECH-800 available?"),
        ("alex", "Where is ORD-9001?"),
        ("alex", "Where is ORD-9004?"),
        ("alex", "Please refund ORD-9001"),
        ("sam", "Please refund ORD-9003"),
        ("lee", "Please refund ORD-9004"),
    ]
    for user, q in tests:
        print(f"{user}: {q}")
        print(f"ShopBot: {run_turn(q, user)}\n")
