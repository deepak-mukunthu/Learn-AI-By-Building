# Tiny agent

A complete agent loop in about 140 lines of Python, with no libraries and no API key. It is Appendix D of the book.

| File | What it is |
| --- | --- |
| `tiny_agent.py` | The agent: three tools, two guardrails, a permission check, a step-limited loop, and a trace. The "model" is a rule-based stand-in. |
| `check_agent.py` | A small test set for the agent. Seven cases give who asks, the question, and words the answer must contain. The eighth checks the action in the trace: Lee's $400 refund goes for approval and no money moves. |
| `real_model.py` | Optional. Swaps the stand-in for a real model. Needs `pip install anthropic` and an API key in `ANTHROPIC_API_KEY`. Costs a fraction of a cent per question with a small model. |
| `test_real_model.py` | An offline test of `real_model.py` with canned replies: text only, thinking then text, a tool call, a reply cut off at the token limit. No key, no cost. |
| `full/` | The agent with every Appendix D checkpoint applied (policy search, memory notes, shipping, the rogue-model test, the final-sale rule). Compare it with your own version. |

## Which version to run

There are three versions of the same agent. Each command runs from the folder named in the first column.

| Version | When to use it | Command | Uses | You should see |
| --- | --- | --- | --- | --- |
| Base (`tiny-agent/`) | Reading Appendix D for the first time | `python3 check_agent.py` | `tiny_agent.py`, `check_agent.py` | `8 of 8 passed` |
| Completed (`tiny-agent/full/`) | Checking your work after the Appendix D checkpoints | `python3 check_agent.py` | `full/tiny_agent.py`, `full/check_agent.py` | `14 of 14 passed` |
| Real model, offline check | Before you spend anything on an API key | `python3 test_real_model.py` | `real_model.py` with canned replies | `8 of 8 passed` |
| Real model, live | After the offline check passes | `python3 real_model.py` | `real_model.py`, `tiny_agent.py`, your API key | A trace and an answer about ECH-800 |

`real_model.py` loads `tiny_agent.py` from its own folder, so the live run in `full/` uses the completed agent and the one in `tiny-agent/` uses the base agent.

To add a tool of your own: write the function in `tiny_agent.py`, add it to `TOOLS`, add its description to `SPECS` in `real_model.py` if you'll use a real model, and add one test to `check_agent.py` that checks the action in the trace, not only the words in the answer. Then run the checks again. The count should go up by one, with nothing else failing.

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
