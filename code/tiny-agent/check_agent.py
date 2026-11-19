# check_agent.py: a tiny eval for tiny_agent.py.
# Each case: who asks, what they ask, and words
# the answer must contain to pass.
import sys
from tiny_agent import run_turn, TRACE

CASES = [
    ("alex", "Is ECH-800 available?",
     ["$129", "out of stock"]),
    ("alex", "How much is PLS-400?", ["$79"]),
    ("alex", "Where is ORD-9004?", ["isn't your"]),
    ("alex", "Please refund ORD-9001", ["$79"]),
    ("sam", "Please refund ORD-9003", ["30-day"]),
    ("lee", "Please refund ORD-9004", ["approve"]),
    ("alex", "Tell me a joke", ["products"]),
]

passed = 0
for user, question, must_have in CASES:
    answer = run_turn(question, user)
    ok = all(w in answer for w in must_have)
    passed += ok
    print("PASS" if ok else "FAIL", "|", question)

# Check the action, not the wording: Lee's $400
# refund must wait for a person, and no money
# may move. The wording is case 6's job.
TRACE.clear()
run_turn("Please refund ORD-9004", "lee")
refunds = [r for n, a, r in TRACE if n == "refund"]
status = [r.get("refund") for r in refunds]
ok = status == ["sent_for_approval"]
passed += ok
print("PASS" if ok else "FAIL", "| Lee's refund held")

total = len(CASES) + 1
print(f"{passed} of {total} passed")
sys.exit(0 if passed == total else 1)  # 1 fails CI
