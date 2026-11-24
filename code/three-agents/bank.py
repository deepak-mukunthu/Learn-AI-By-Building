# bank.py: an invented banking assistant. Same
# loop as ShopBot, different settings.
NAME = "BankBot"

# ---- Context: instructions ----------------------
SYSTEM = ("You are BankBot. Answer only about the "
          "customer's own accounts, from tool "
          "results. Never give financial advice.")
FALLBACK = ("I can help with balances, transactions, "
            "and cards. What do you need?")

# ---- Data the tools can reach -------------------
ACCOUNTS = {
    "ACC-1001": {"customer": "alex", "balance": 2450,
                 "card": "active",
                 "last": ["coffee $4", "rent $1,200"]},
    "ACC-1002": {"customer": "sam", "balance": 310,
                 "card": "frozen",
                 "last": ["groceries $62"]},
}

# ---- Tools, with the rules in code --------------
def get_account(account_id, user):
    acct = ACCOUNTS.get(account_id)
    if acct is None:
        return {"error": f"no account {account_id}"}
    # Identity: customers see only their accounts.
    if acct["customer"] != user:
        return {"error": "that isn't your account"}
    return {"account_id": account_id, **acct}

def freeze_card(account_id, user):
    acct = get_account(account_id, user)
    if "error" in acct:
        return acct
    ACCOUNTS[account_id]["card"] = "frozen"
    return {"status": "frozen"}  # safe: self-serve

def unfreeze_card(account_id, user):
    acct = get_account(account_id, user)
    if "error" in acct:
        return acct
    # Rule in code: only a person may unfreeze.
    return {"status": "sent_to_person"}

TOOLS = {"get_account": get_account,
         "freeze_card": freeze_card,
         "unfreeze_card": unfreeze_card}
NEEDS_USER = {"get_account", "freeze_card",
              "unfreeze_card"}

# ---- Which tool a question needs ----------------
ACC = r"ACC-[0-9]+"
ROUTES = [
    (ACC, "unfreeze", "unfreeze_card", "account_id"),
    (ACC, "freeze", "freeze_card", "account_id"),
    (ACC, None, "get_account", "account_id"),
]

# ---- Model: how it words a tool result ----------
def answer(data):
    if "error" in data:
        return {"answer": "Sorry, I can't do that: "
                + data["error"] + "."}
    if data.get("status") == "frozen":
        return {"answer": "Your card is frozen. "
                "No new payments will go through."}
    if data.get("status") == "sent_to_person":
        return {"answer": "For your safety, a person "
                "has to unfreeze a card. I've asked "
                "the team to call you."}
    last = ", ".join(data["last"])
    return {"answer": f"Your balance is "
            f"${data['balance']:,}. Recent: {last}."}
