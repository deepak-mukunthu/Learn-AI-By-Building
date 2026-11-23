# Projects used in the book

All projects are open source. Most need nothing beyond Python or Node.js. Check each project's own README for the exact steps, and see Appendix B of the book for the quick reference.

You need only the first one, the AI Builder Lab, to follow the chapters. It runs in a browser with nothing to install. The rest are optional, and each deepens a single chapter.

## Match the book's version

Each repository has a release tagged `book-edition-1`, the version the book's figures and outputs came from. If you clone with Git, run `git checkout book-edition-1` inside the new folder before anything else. Git's note about a "detached HEAD" is expected.

If you download a ZIP instead, don't use the green Code button, which gives you the latest version. Click **Releases** on the repository's page, open `book-edition-1`, and download **Source code (zip)**.

This repository works the same way: it holds the tiny agent from Appendix D (`code/tiny-agent`, with every checkpoint applied in `code/tiny-agent/full`) and the templates.

## Every project in the book

| Project | Chapters | What it teaches | Needs | API key? |
| --- | --- | --- | --- | --- |
| [AI-Builder-Lab](https://github.com/deepak-mukunthu/AI-Builder-Lab) (ShopBot and the Sandbox) | 2 to 10, Appendix G | The whole agent, with planted problems to find and fix. Its Sandbox screen lets you set up a small assistant with forms and watch the five parts change its answers | A browser | No |
| [RAG-Explorer](https://github.com/deepak-mukunthu/RAG-Explorer) | 4 | Compare ways of chunking and searching your own documents | Python and Node.js | Optional |
| [AgentTown](https://github.com/deepak-mukunthu/AgentTown) | 5, 7 | Memory and many agents in one simulation | Node.js | No, for the demo |
| [AI-RedTeaming-Framework](https://github.com/deepak-mukunthu/AI-RedTeaming-Framework) | 7 | Run 12 attack tests against a sample assistant and read the report | Python | Yes, a few cents per run |
| [HarnessEval](https://github.com/deepak-mukunthu/HarnessEval) | 8 | Run the same model inside five harnesses and compare the results | Python | Optional |
| [AIEvalsTutor](https://github.com/deepak-mukunthu/AIEvalsTutor) | 8 | An interactive tutorial on designing evals, from simple checks to model judges | Node.js | Yes |
| [RealSim](https://github.com/deepak-mukunthu/RealSim) | 8 | Why simulated testing needs many runs | Python | No, for the demo |
| [SelfOptimizingAgent](https://github.com/deepak-mukunthu/SelfOptimizingAgent) | 9 | An improvement loop that proposes changes to an agent and tests them | Python | No, in demo mode |
| [AI-Cost-Optimization](https://github.com/deepak-mukunthu/AI-Cost-Optimization) | 10 | Tokens, strategies, and what each saves | Node.js | No |
| [ai-transformation-center](https://github.com/deepak-mukunthu/ai-transformation-center) | 11 | Model how a workflow's numbers change as AI takes on more of the work | A browser | No |
| [moat-evaluator](https://github.com/deepak-mukunthu/moat-evaluator) | 12 | Score how hard an AI product would be to copy | Node.js | No |

Not used in the book, but useful for product managers: [AINativePM](https://github.com/deepak-mukunthu/AINativePM), workflows and templates for product managers. It has no `book-edition-1` release.

## Opening the lab

On the lab's GitHub page, click **Releases**, open `book-edition-1`, download **Source code (zip)**, and unzip it. Then double-click `index.html`. It works straight from the file, with no terminal, server or account. The menu on the left has nine screens. **Sandbox** is the last one.

The ShopBot screens don't save your progress between page reloads. To start over, reload the page, or use **Reset agent to v1** on the Simulate screen. If you edit `js/domain.js` or `js/scenarios.js`, save the file and reload the page to see the change. The Sandbox keeps its work in your browser; use **Export JSON** to save a copy.

The folder also has `serve.py`, an optional local web server. You need it only for the Sandbox's "Use your own model" mode with a model on your own computer, such as Ollama, which refuses pages opened from a file. Run `python3 serve.py` in the folder and open http://localhost:8777.

## Starting any other project

Open a terminal, `cd` to the folder where you keep projects, and clone it:

```
git clone https://github.com/deepak-mukunthu/<project-name>.git
cd <project-name>
git checkout book-edition-1
```

Then follow that project's README. Projects with a web page start a small server and print an address such as http://localhost:3000. Press Ctrl+C in the terminal to stop it.

For Python projects, create a private set of libraries first:

```
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Node projects use `npm install`.

Projects that can use a real model read the key from a file named `.env` in the project folder. Most include an example file; copy it with `cp .env.example .env` (Windows: `copy .env.example .env`), open `.env` in a text editor, and paste your key after the equals sign. Never share or upload this file.

## Common problems

| You see | What it means | Try this |
| --- | --- | --- |
| `command not found: git` (or `python3`, `node`) | The tool isn't installed, or the terminal can't find it | Install it, then close and reopen the terminal |
| `Address already in use` or "port in use" | Another program, often an earlier copy of the same project, is using that address | Find the old terminal window and press Ctrl+C, or restart your computer |
| The browser says "can't connect" | The project's server isn't running, or the address is wrong | Check the terminal is still running it, and that the address matches exactly, including the number |
| `No such file or directory` | The terminal is in the wrong folder | Run `cd` and the project's folder name first, or check the folder name with `ls` (Mac) or `dir` (Windows) |
| `Permission denied` on `./demo.sh` | The script isn't marked as runnable | Run `chmod +x demo.sh`, then try again |
| Your edit to `domain.js` didn't change anything | The file wasn't saved, or the page wasn't reloaded | Save, then reload the browser page. If it still doesn't change, look for a typo, such as a missing comma |
| The lab shows only part of the page, or no menu | It was opened from inside the zip, or files were moved | Unzip the whole download, then double-click `index.html` in the unzipped folder |
| The page is blank after an edit | The edit broke the file's syntax | Undo your last change and try again. Most often it's a missing comma or bracket |
| Your numbers don't match the book | Fixes were applied in a different order, or a file was edited | Reset to v1, undo any file edits, and apply fixes in the book's order |
