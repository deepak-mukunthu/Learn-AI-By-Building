# helpdesk.py: an invented IT help desk. Same
# loop as ShopBot, different settings.
NAME = "HelpDesk"

# ---- Context: instructions ----------------------
SYSTEM = ("You are the IT help desk. IT questions "
          "only. Never ask for or repeat a password.")
FALLBACK = ("I can help with tickets, outages, and "
            "password resets. What do you need?")

# ---- Data the tools can reach -------------------
EMPLOYEES = {
    "alex": {"verified": True, "executive": False},
    "lee": {"verified": True, "executive": True},
    "sam": {"verified": False, "executive": False},
}
TICKETS = {
    "TKT-501": {"employee": "alex", "status": "open",
                "topic": "wifi drops at desk 4B"},
}
OUTAGES = {"VPN": "down since 09:10",
           "EMAIL": None, "WIFI": None}

# ---- Tools, with the rules in code --------------
def get_ticket(ticket_id, user):
    t = TICKETS.get(ticket_id)
    if t is None:
        return {"error": f"no ticket {ticket_id}"}
    if t["employee"] != user:
        return {"error": "that isn't your ticket"}
    return {"ticket_id": ticket_id, **t}

def outage_status(service):
    return {"service": service,
            "outage": OUTAGES.get(service)}

def reset_password(user):
    who = EMPLOYEES.get(user, {})
    # Identity checked in code, before any reset.
    if not who.get("verified"):
        return {"error": "your identity isn't "
                "verified yet"}
    if who.get("executive"):  # routed to a person
        return {"status": "sent_to_person"}
    return {"status": "reset_link_sent"}

TOOLS = {"get_ticket": get_ticket,
         "outage_status": outage_status,
         "reset_password": reset_password}
NEEDS_USER = {"get_ticket", "reset_password"}

# ---- Which tool a question needs ----------------
ROUTES = [
    (None, "password", "reset_password", None),
    (r"TKT-[0-9]+", None, "get_ticket", "ticket_id"),
    (r"VPN|EMAIL|WIFI", None, "outage_status",
     "service"),
]

# ---- Model: how it words a tool result ----------
def answer(data):
    if "error" in data:
        return {"answer": "Sorry, I can't do that: "
                + data["error"] + "."}
    if data.get("status") == "reset_link_sent":
        return {"answer": "I've sent a reset link to "
                "your work phone."}
    if data.get("status") == "sent_to_person":
        return {"answer": "Resets for your account "
                "go through a person. I've asked the "
                "team to call you."}
    if "service" in data:
        if data["outage"]:
            return {"answer": f"{data['service']} is "
                    f"{data['outage']}. We're on it."}
        return {"answer": f"No known outage for "
                f"{data['service']}."}
    return {"answer": f"Ticket {data['ticket_id']} "
            f"({data['topic']}) is {data['status']}."}
