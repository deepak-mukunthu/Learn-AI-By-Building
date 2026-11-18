# Learn AI by Building: Companion Repository

Code, templates, and guides that go with the book **Learn AI by Building: A Practical Guide for Product Managers, Developers, and Builders** by Deepak Mukunthu.

The book teaches AI through one running assistant, ShopBot, and seven skills: understand the model, see the whole system, find the real cause of a failure, give it the right information, connect it to real systems safely, prove it works, and make it affordable. This repository holds everything you can copy, run, and adapt while you read. You don't need the book to use the templates, but the chapter guide shows where each piece fits.

The habit that connects it all: when an AI product gives a wrong answer, check the parts around the model before you blame the model.

## Start in ten minutes, with nothing to install

1. Open the [ai-builder-sandbox](https://github.com/deepak-mukunthu/ai-builder-sandbox) project. Click **Code**, then **Download ZIP**, unzip it, and double-click `index.html`.
2. Choose **ShopBot mini**, click **Load broken version**, open the **5 Test** tab, and click **Run all tests**. The score is 30%.
3. Open a failing test's trace, find the part that's missing something, fix it, and run the tests again. Five fixes take the score to 100%.

The sandbox's "model" is a simulator that follows fixed rules, so everyone gets the same results. Real models are less predictable, and the book explains how to handle that.

## What's here

| Folder | What it holds | Book reference |
| --- | --- | --- |
| [`code/tiny-agent/`](code/tiny-agent/) | A complete agent loop in about 140 lines of Python, a test set, and an optional real-model version. No libraries needed. | Appendix D, Appendix F |
| [`templates/`](templates/) | Job card, test case sheet, debugging checklist, system prompt skeleton, weekly improvement hour | Appendix A, Appendix E |
| [`templates/product-managers/`](templates/product-managers/) | One-page AI feature spec, questions for engineers, rollout and metrics, cost and benefit worksheet | Appendix H |
| [`templates/builders/`](templates/builders/) | Ten help-desk test questions and a day-by-day 30-day checklist | Appendix G |
| [`docs/chapter-guide.md`](docs/chapter-guide.md) | What to do in each chapter, where, and what you should see | All chapters |
| [`docs/projects.md`](docs/projects.md) | Every open-source project the book uses, with setup and common problems | Chapter 12, Appendix B |

## Which path is yours?

| If you're a | Start with | Then |
| --- | --- | --- |
| **Product manager** | The sandbox, then [`templates/product-managers/`](templates/product-managers/) | Fill in the AI feature spec for a real idea, and take the questions for engineers to your next design review |
| **Developer** | [`code/tiny-agent/`](code/tiny-agent/), then the [ShopBot lab](https://github.com/deepak-mukunthu/data-flywheel-agent-lab) | Add a tool and a test case, then swap in a real model with `real_model.py` |
| **Builder** | The sandbox, then [`templates/builders/`](templates/builders/) | Build the help-desk assistant on a platform you already use, with the ten test questions |

## Run the tiny agent

```
cd code/tiny-agent
python3 tiny_agent.py
python3 check_agent.py
```

You need Python 3 and nothing else. You should see traces for each question and `7 of 7 passed` at the end. On Windows, use `python` instead of `python3`.

## Related projects

The book uses a path of small open-source projects. The full list, with setup steps, is in [`docs/projects.md`](docs/projects.md). The main ones:

- [ai-builder-sandbox](https://github.com/deepak-mukunthu/ai-builder-sandbox): configure a small assistant with forms, no install
- [data-flywheel-agent-lab](https://github.com/deepak-mukunthu/data-flywheel-agent-lab): ShopBot, with planted problems to find and fix
- [RAG-Explorer](https://github.com/deepak-mukunthu/RAG-Explorer): chunking and search
- [AI-RedTeaming-Framework](https://github.com/deepak-mukunthu/AI-RedTeaming-Framework): test an agent's guardrails
- [AI-Cost-Optimization](https://github.com/deepak-mukunthu/AI-Cost-Optimization): tokens and cost
- [AINativePM](https://github.com/deepak-mukunthu/AINativePM): workflows and templates for product managers

## About the numbers

ShopBot's numbers come from a deterministic simulator, so you'll get exactly the numbers the book reports. The simulator is a teaching tool with planted problems, not a benchmark of any real product. All companies, policies, orders, and prices in the examples are fictional.

## Contributing

Found a typo, a broken step, or a template that could be clearer? Open an issue or a pull request. Small, focused changes are easiest to review.

## License

MIT. See [LICENSE](LICENSE). The templates may be copied and adapted for your own use. The text of the book is separate and is not included here.

## Author

Deepak Mukunthu. Newsletter: [deepakmukunthu.substack.com](https://deepakmukunthu.substack.com).
