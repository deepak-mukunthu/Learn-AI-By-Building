# check_agent.py: a tiny eval for tiny_agent.py.
# Each case: who asks, what they ask, and words
# the answer must contain to pass.
from tiny_agent import run_turn

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
print(f"{passed} of {len(CASES)} passed")
