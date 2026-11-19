# tiny_agent.py: a complete agent loop in one file.
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
}
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
    if order["days_ago"] > REFUND_DAYS:
        return {"error": "past the 30-day window"}
    if order["total"] > REFUND_LIMIT:
        return {"refund": "sent_for_approval",
                "amount": order["total"]}
    return {"refund": "done", "amount": order["total"]}

TOOLS = {"get_product": get_product,
         "get_order": get_order,
         "refund": refund}
NEEDS_USER = {"get_order", "refund"}  # who asks

# ---- 3. The model (a fake one, for now) ----------
SKU = re.compile(r"[A-Z]{3}-[0-9]{3}")  # ECH-800

def fake_model(messages):
    """Reads the conversation and returns either a
    tool request or a final answer, as a real model
    would. Simple rules stand in for prediction."""
    last = messages[-1]
    if last["role"] == "tool":
        return answer_from(json.loads(last["content"]))
    words = last["content"].replace("?", " ").split()
    for w in words:
        if SKU.fullmatch(w):  # any SKU, real or not
            return {"tool": "get_product",
                    "args": {"sku": w}}
        if w.startswith("ORD-"):
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

def run_turn(question, user, model=fake_model):
    messages = [{"role": "system", "content": SYSTEM},
                {"role": "user", "content": question}]
    for step in range(5):  # stop runaway loops
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
