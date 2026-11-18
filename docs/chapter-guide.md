# Chapter guide

What you do in each chapter, where to do it, and what you should see. "Sandbox" means [ai-builder-sandbox](https://github.com/deepak-mukunthu/ai-builder-sandbox), which needs no install. "Lab" means [data-flywheel-agent-lab](https://github.com/deepak-mukunthu/data-flywheel-agent-lab), run with `python3 serve.py` at http://localhost:8777.

## Part I. How AI works

| Ch | Title | Do | Where | You should see |
| --- | --- | --- | --- | --- |
| 1 | What a Model Actually Does | Count tokens, change temperature, test what a model can and can't know | Any AI chat app | The same question gives different wording at different temperatures. The model knows nothing you didn't send it. |
| 2 | From Chatbot to Agent | Run ShopBot and make it fail | Lab, or sandbox with ShopBot mini | A first quality score of 76 out of 100. Task success is only 27% even though intent accuracy and grounding are 100%. |
| 3 | Your First Debugging Session | Open scenario S11 and guess which part failed for five traces | Lab (Traces & Tagging) | Five complaints, five different parts, and none of them the model. |

## Part II. Build the parts around the model

| Ch | Title | Do | Where | You should see |
| --- | --- | --- | --- | --- |
| 4 | Context | Fix the missing products (`catalogTopK` 3 to 8) | Lab, or sandbox Help desk, tab 2 Knowledge | Quality 80. S03 now says the Echo Studio Mic is out of stock. Task success rises from 27% to 60%. |
| 5 | Memory | Turn memory on and check what it keeps | Lab, or sandbox tab 3 Memory | The assistant stops asking for what it already knows. |
| 6 | Tools | Find the stale price and fix its source | Lab, or sandbox tab 4 Tools & Rules | The price comes from the tool, so it follows the data. |
| 7 | Guardrails | Enforce the refund limit in code | Lab, or sandbox tab 4 | The $400 refund goes to a person. By the end of this chapter the lab score is 98. |

## Part III. Test it, improve it, afford it

| Ch | Title | Do | Where | You should see |
| --- | --- | --- | --- | --- |
| 8 | Evals | Read a test case, add one of your own, change the weights | Lab (js/scenarios.js), or sandbox tab 5 Test | Six checks that add up to one score, and a fix you can measure. |
| 9 | Traces and the Improvement Loop | Run one turn of the weekly loop | Lab, or sandbox tab 5 with the Trace buttons | The lab reaches 100 after the last fix. |
| 10 | What It Costs | Run the cost simulator, then redo the worked example on paper | [AI-Cost-Optimization](https://github.com/deepak-mukunthu/AI-Cost-Optimization) | About 3.06 million tokens and $16.10 for the baseline session, and about 469,000 tokens and $0.78 with all strategies on. |

## Part IV. Build your own

| Ch | Title | Do | Where | You should see |
| --- | --- | --- | --- | --- |
| 11 | Your First 30 Days | Fill in a job card, write a test sheet, set a go/no-go rule | [templates/](../templates/) | A one-page plan with numbers you wrote down before building. |
| 12 | Keep Building | Pick a project from the path and run it | [projects.md](projects.md) | One more project running, and one change you predicted before making it. |

## Appendices

| Appendix | Topic | Companion material |
| --- | --- | --- |
| A | Starter templates | [templates/](../templates/) |
| B | Project guides and troubleshooting | [projects.md](projects.md) |
| D | Build a tiny agent from scratch | [code/tiny-agent/](../code/tiny-agent/) |
| E | A prompt workshop | [templates/system-prompt-skeleton.md](../templates/system-prompt-skeleton.md) |
| F | For developers | [code/tiny-agent/real_model.py](../code/tiny-agent/real_model.py) |
| G | For builders | [templates/builders/](../templates/builders/) |
| H | For product managers | [templates/product-managers/](../templates/product-managers/) |

The lab's numbers come from a deterministic simulator, so you get exactly the numbers above. The simulator is a teaching tool with planted problems, not a benchmark of any real product.
