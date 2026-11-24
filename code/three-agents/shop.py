# shop.py: ShopBot's settings, the same agent as
# ../tiny-agent/tiny_agent.py, without the loop.
NAME = "ShopBot"

# ---- Context: instructions ----------------------
SYSTEM = ("You are ShopBot. Answer only from tool "
          "results. Never guess prices.")
FALLBACK = ("I can help with products and orders. "
            "What do you need?")

# ---- Data the tools can reach -------------------
CATALOG = {
    "ECH-800": {"name": "Echo Studio Mic",
                "price": 129, "stock": 0},
    "PLS-400": {"name": "Pulse Earbuds",
                "price": 79, "stock": 120},
}
ORDERS = {
    "ORD-9001": {"customer": "alex", "total": 79,
                 "days_ago": 5},
    "ORD-9003": {"customer": "sam", "total": 129,
                 "days_ago": 45},
    "ORD-9004": {"customer": "lee", "total": 400,
                 "days_ago": 3},
}
REFUND_DAYS = 30    # refund window
REFUND_LIMIT = 150  # above this, a person approves

# ---- Tools, with the rules in code --------------
def get_product(sku):
    item = CATALOG.get(sku)
    if item is None:
        return {"error": f"no product {sku}"}
    return {"sku": sku, **item}

def get_order(order_id, user):
    order = ORDERS.get(order_id)
    if order is None:
        return {"error": f"no order {order_id}"}
    if order["customer"] != user:
        return {"error": "that isn't your order"}
    return {"order_id": order_id, **order}

def refund(order_id, user):
    order = get_order(order_id, user)
    if "error" in order:
        return order
    if order["days_ago"] > REFUND_DAYS:
        return {"error": "past the 30-day window"}
    if order["total"] > REFUND_LIMIT:
        return {"status": "sent_to_person",
                "amount": order["total"]}
    return {"status": "done", "amount": order["total"]}

TOOLS = {"get_product": get_product,
         "get_order": get_order, "refund": refund}
NEEDS_USER = {"get_order", "refund"}

# ---- Which tool a question needs ----------------
# (id pattern, word the question must contain,
#  tool, argument name)
ROUTES = [
    (r"[A-Z]{3}-[0-9]{3}", None, "get_product", "sku"),
    (r"ORD-[0-9]+", "refund", "refund", "order_id"),
    (r"ORD-[0-9]+", None, "get_order", "order_id"),
]

# ---- Model: how it words a tool result ----------
def answer(data):
    if "error" in data:
        return {"answer": "Sorry, I can't do that: "
                + data["error"] + "."}
    if data.get("status") == "done":
        return {"answer": "Done. I've refunded "
                f"${data['amount']}."}
    if data.get("status") == "sent_to_person":
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
