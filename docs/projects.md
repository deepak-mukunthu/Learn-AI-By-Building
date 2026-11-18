# Projects used in the book

All projects are open source. Most need nothing beyond Python or Node.js. Check each project's own README for the exact steps.

| Project | Chapters | What it teaches | Needs | API key? |
| --- | --- | --- | --- | --- |
| [ai-builder-sandbox](https://github.com/deepak-mukunthu/ai-builder-sandbox) | 2, 4 to 11, Appendix G | Set up a small assistant with forms and watch the five parts change its answers | A browser | No |
| [data-flywheel-agent-lab](https://github.com/deepak-mukunthu/data-flywheel-agent-lab) (ShopBot) | 2 to 9 | The whole agent, with planted problems to find and fix | Python | No |
| [RAG-Explorer](https://github.com/deepak-mukunthu/RAG-Explorer) | 4 | Compare ways of chunking and searching your own documents | Python and Node.js | Optional |
| [AgentTown](https://github.com/deepak-mukunthu/AgentTown) | 5, 7 | Memory and many agents in one simulation | Node.js | No, for the demo |
| [AI-RedTeaming-Framework](https://github.com/deepak-mukunthu/AI-RedTeaming-Framework) | 7 | Attack your own agent to test its guardrails | Python | Yes, a few cents per run |
| [HarnessEval](https://github.com/deepak-mukunthu/HarnessEval) | 8 | Compare five strategies with one evaluation harness | Python | Optional |
| [AIEvalsTutor](https://github.com/deepak-mukunthu/AIEvalsTutor) | 8 | A tutorial on evals for beginners and practitioners | Node.js | Yes |
| [RealSim](https://github.com/deepak-mukunthu/RealSim) | 8 | Simulation at scale | Python | No, for the demo |
| [SelfOptimizingAgent](https://github.com/deepak-mukunthu/SelfOptimizingAgent) | 9 | The improvement loop, automated | Python | No, in demo mode |
| [AI-Cost-Optimization](https://github.com/deepak-mukunthu/AI-Cost-Optimization) | 10 | Tokens, strategies, and what each saves | Node.js | No |
| [ai-transformation-center](https://github.com/deepak-mukunthu/ai-transformation-center) | 11 | Model how a workflow's numbers change as AI takes on more of the work | A browser | No |
| [moat-evaluator](https://github.com/deepak-mukunthu/moat-evaluator) | 12 | Score how hard an AI product would be to copy | Node.js | No |
| [AINativePM](https://github.com/deepak-mukunthu/AINativePM) | 11, Appendix H | Workflows and templates for product managers | Varies | Varies |

## Starting any project

```
git clone https://github.com/deepak-mukunthu/<project-name>.git
cd <project-name>
```

Then follow that project's README. For Python projects, create a private set of libraries first:

```
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Projects that can use a real model read the key from a file named `.env` in the project folder. Copy the example with `cp .env.example .env`, add your key, and never commit that file.

## Common problems

| You see | Likely cause | Fix |
| --- | --- | --- |
| `command not found: git`, `python3`, or `node` | The tool isn't installed, or the terminal was open during the install | Install it, then open a new terminal |
| `No such file or directory` | You're one folder off | Run `pwd`, then `cd` into the project folder |
| `Address already in use` | An earlier copy is still running | Press Ctrl+C in the other terminal, or use that copy |
| Python isn't found on Windows | "Add python.exe to PATH" wasn't ticked | Run the installer again and tick it |
| A blank page after editing a file | A missing comma or brace | Undo your last edit and look at the line you changed |
