# Chapter guide

What you do in each chapter, where to do it, and what you should see. "Sandbox" means [AI-Builder-Sandbox](https://github.com/deepak-mukunthu/AI-Builder-Sandbox), which needs no install. "Lab" means [AI-Data-Flywheel](https://github.com/deepak-mukunthu/AI-Data-Flywheel) (ShopBot), run with `python3 serve.py` at http://localhost:8777.

Match the book's version. After cloning any project, run `git checkout book-edition-1`, or download the `book-edition-1` release ZIP from the project's Releases page. See [projects.md](projects.md).

## Part I. How AI works

| Ch | Title | Do | Where | You should see |
| --- | --- | --- | --- | --- |
| 1 | What a Model Actually Does | Three ten-minute experiments: test statelessness, missing facts, and randomness | Any AI chat app | A new chat doesn't know your favorite color. An invented price for a store the model can't know. Varied coffee shop names, but 391 for 17 × 23. |
| 2 | From Chatbot to Agent | Run ShopBot on your laptop | Lab, or sandbox with ShopBot mini | Quality 76 out of 100, from 15 conversations. Task success is only 27%. |
| 3 | Your First Debugging Session | Play the guessing game: open five failed conversations in Traces & Tagging and guess which part failed | Lab, or sandbox ShopBot mini with Load broken version | Five failures, and none of them is the model. S03, S04, and S12 are context failures. S11 and S10 are harness failures. S09 is a memory failure only. |

## Part II. Build the parts around the model

| Ch | Title | Do | Where | You should see |
| --- | --- | --- | --- | --- |
| 4 | Context: What the Model Sees | Apply the "Catalog truncated in context window" fix (`catalogTopK` 3 to 8) | Lab, or sandbox Help desk, tab 2 Knowledge | v2 at quality 80, up from 76. S03 now says the Echo Studio Mic is out of stock. Task success rises from 27% to 60%. |
| 5 | Memory: What the Agent Keeps | Turn on customer profile memory, then lower the temperature | Lab, or sandbox ShopBot mini, tab 3 Memory | v3: "No re-ask" goes from 67% to 100%, quality 82. v4: quality stays at 82, and p95 latency drops from 588 to 451 milliseconds. |
| 6 | Tools: Where the Facts Come From | Switch the pricing source from stale to live | Lab, or sandbox ShopBot mini, tab 4 Tools & Rules | The tool step reads "$69" with a source of "live". v5 shows quality 91, up from 82, and grounding back at 100%. |
| 7 | Guardrails: Rules That Hold | Enable the refund guardrail | Lab (scenario S11), or sandbox ShopBot mini, tab 4 | The $400 refund goes to a person for approval. Policy safety goes from 87% to 100%, and quality reads 98. |

## Part III. Test it, improve it, afford it

| Ch | Title | Do | Where | You should see |
| --- | --- | --- | --- | --- |
| 8 | Evals: How You Know It Works | Run 5× repeats, then add a sixteenth case (S16) in `js/scenarios.js` | Lab, or sandbox tab 5 Test | 75 traces (15 scenarios times 5). At v1, quality 76 and task success 27%. S16 fails at v1 on task success only (5 of 6 checks) and passes from v5 on. |
| 9 | Traces and the Improvement Loop | Finish ShopBot: raise recall accuracy (v7), then apply the scoped system prompt (v8) | Lab, or sandbox tab 5 with the Trace buttons | After v7, quality stays at 98. After v8, scope and task success read 100% and quality reads 100. |
| 10 | What It Costs | Run the cost simulator, or redo the worked example on paper | [AI-Cost-Optimization](https://github.com/deepak-mukunthu/AI-Cost-Optimization), or the sandbox cost strip | About 3.06 million tokens and $16.10 for the 50-turn baseline, and about 469,000 tokens and $0.78 with all strategies on. |

## Part IV. Build your own

| Ch | Title | Do | Where | You should see |
| --- | --- | --- | --- | --- |
| 11 | Your First 30 Days | Write your job card | [templates/job-card.md](../templates/job-card.md) | One page with nine filled lines. |
| 12 | Keep Building | Pick a project from the path and run it | [projects.md](projects.md) | One more project running, and one change you predicted before making it. |

## Appendices

| Appendix | Topic | Companion material |
| --- | --- | --- |
| A | Starter templates (A1 job card, A2 test case sheet, A3 debugging checklist, A4 system prompt skeleton, A5 weekly improvement hour, A6 My Assistant worksheet, A7 Northwind document pack) | [templates/](../templates/) |
| B | Project guides and troubleshooting | [projects.md](projects.md) |
| C | Answers to "Check Yourself" | In the book |
| D | Build a tiny agent from scratch | [code/tiny-agent/](../code/tiny-agent/). The `full` folder, [code/tiny-agent/full/](../code/tiny-agent/full/), has every checkpoint applied, and its `check_agent.py` runs 14 checks. The top-level `check_agent.py` prints 8 of 8 passed. |
| E | A prompt workshop | [templates/system-prompt-skeleton.md](../templates/system-prompt-skeleton.md) |
| F | For developers | [code/tiny-agent/real_model.py](../code/tiny-agent/real_model.py), and [code/tiny-agent/test_real_model.py](../code/tiny-agent/test_real_model.py), an offline test (8 checks, no key, no cost) that should print 8 of 8 passed |
| G | For builders | [templates/builders/](../templates/builders/) |
| H | For product managers | [templates/product-managers/](../templates/product-managers/) |

The lab's numbers come from a deterministic simulator, so you get exactly the numbers above when you apply the fixes in the book's order. The simulator is a teaching tool with planted problems, not a benchmark of any real product.
