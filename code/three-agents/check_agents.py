# check_agents.py: one set of checks per agent,
# run through the same loop.
import sys
import bank
import helpdesk
import shop
from agent_loop import run_turn

CASES = [
    (shop, "alex", "Is ECH-800 available?",
     ["$129", "out of stock"]),
    (shop, "alex", "Where is ORD-9004?",
     ["isn't your"]),
    (shop, "sam", "Please refund ORD-9003", ["30-day"]),
    (shop, "lee", "Please refund ORD-9004",
     ["approve"]),
    (bank, "alex", "What's my balance on ACC-1001?",
     ["$2,450"]),
    (bank, "alex", "Show ACC-1002", ["isn't your"]),
    (bank, "sam", "Unfreeze the card on ACC-1002",
     ["a person"]),
    (bank, "alex", "Should I buy shares?",
     ["balances"]),
    (helpdesk, "alex", "Is the VPN down?", ["09:10"]),
    (helpdesk, "alex", "Status of TKT-501?", ["open"]),
    (helpdesk, "sam", "Please reset my password",
     ["isn't verified"]),
    (helpdesk, "lee", "Please reset my password",
     ["a person"]),
]

# Check actions, not words: a rule that holds
# leaves the data unchanged.
def held(agent, user, question, tool, status):
    trace = []
    run_turn(agent, question, user, trace)
    got = [r.get("status") for n, a, r in trace
           if n == tool]
    return got == [status]

ACTIONS = [
    ("Lee's $400 refund waits for a person",
     held(shop, "lee", "Please refund ORD-9004",
          "refund", "sent_to_person")),
    ("Sam's card stays frozen",
     held(bank, "sam", "Unfreeze ACC-1002",
          "unfreeze_card", "sent_to_person")
     and bank.ACCOUNTS["ACC-1002"]["card"] == "frozen"),
    ("Lee's reset goes to a person",
     held(helpdesk, "lee", "Reset my password",
          "reset_password", "sent_to_person")),
]

passed = 0
for agent, user, question, must_have in CASES:
    answer = run_turn(agent, question, user)
    ok = all(w in answer for w in must_have)
    passed += ok
    print("PASS" if ok else "FAIL", "|", agent.NAME,
          "|", question)
for label, ok in ACTIONS:
    passed += ok
    print("PASS" if ok else "FAIL", "|", label)

total = len(CASES) + len(ACTIONS)
print(f"{passed} of {total} passed")
sys.exit(0 if passed == total else 1)
