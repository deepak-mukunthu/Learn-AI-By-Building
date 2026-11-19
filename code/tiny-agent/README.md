# Tiny agent

A complete agent loop in about 140 lines of Python, with no libraries and no API key. It is Appendix D of the book.

| File | What it is |
| --- | --- |
| `tiny_agent.py` | The agent: three tools, two guardrails, a permission check, a step-limited loop, and a trace. The "model" is a rule-based stand-in. |
| `check_agent.py` | A small test set for the agent. Seven cases give who asks, the question, and words the answer must contain. The eighth checks the action in the trace: Lee's $400 refund goes for approval and no money moves. |
| `real_model.py` | Optional. Swaps the stand-in for a real model. Needs `pip install anthropic` and an API key in `ANTHROPIC_API_KEY`. Costs a fraction of a cent per question with a small model. |
| `test_real_model.py` | An offline test of `real_model.py` with canned replies: text only, thinking then text, a tool call, a reply cut off at the token limit. No key, no cost. |
| `full/` | The agent with every Appendix D checkpoint applied (policy search, memory notes, shipping, the rogue-model test, the final-sale rule). Compare it with your own version. |

## Run it

```
python3 tiny_agent.py
python3 check_agent.py
```

On Windows, use `python` instead of `python3`. You should see traces for each question and `8 of 8 passed` from the checks.

Before you try a real model, run `python3 test_real_model.py`. It should print `8 of 8 passed`. In `full/`, `python3 check_agent.py` should print `14 of 14 passed`.

## Exercises

1. Add a test case of your own to `check_agent.py` and run it.
2. Remove the refund-limit check from the agent, run the tests, and see which fail. Put it back.
3. Add a `cancel_order` tool that needs approval, with one test that should succeed and one that should be refused.
4. Write each turn's messages to a file and find the cause of a wrong answer in it.
5. Run `real_model.py` five times and find the least stable test case.

The data matches the ShopBot lab: Echo Studio Mic $129 (out of stock), Pulse Earbuds $79, orders ORD-9001, ORD-9003 and ORD-9004 (and ORD-9006, a final-sale cable, in `full/`), a 30-day refund window, and a $150 approval limit.
