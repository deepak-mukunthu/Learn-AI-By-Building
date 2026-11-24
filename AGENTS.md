# AGENTS.md

Notes for AI agents and coding assistants that open this repository, usually on behalf of a reader of the book *Learn AI by Building* by Deepak Mukunthu.

## What this is

The companion repository for the book. It holds the code, templates and guides a reader copies, runs and adapts. The book text is not here.

The book has three reader paths (product manager, developer, builder) and one habit: when an AI product gives a wrong answer, check the parts around the model (context, memory, tools, harness) before blaming the model.

## Layout

```
code/tiny-agent/            an agent loop in plain Python (Appendix D, F)
  tiny_agent.py             the agent
  check_agent.py            8 checks
  real_model.py             optional real-model version
  test_real_model.py        offline test for it, canned replies
  full/                     the agent with every Appendix D checkpoint
templates/                  job card, test case sheet, debugging checklist,
                            system prompt skeleton, weekly improvement hour,
                            My Assistant worksheet (Appendix A, E)
templates/product-managers/ feature spec, questions for engineers, rollout,
                            cost and benefit (Appendix H)
templates/builders/         Northwind documents, help-desk test questions,
                            30-day checklist (Appendix A7, G)
docs/chapter-guide.md       what to do in each chapter and what to expect
docs/projects.md            every project the book uses, with setup
llms.txt                    index of this repository for language models
```

## Run it

Python 3 only, no packages. On Windows use `python`.

| Directory | Command | Expect |
| --- | --- | --- |
| `code/tiny-agent/` | `python3 check_agent.py` | `8 of 8 passed` |
| `code/tiny-agent/` | `python3 test_real_model.py` | `8 of 8 passed`, no network |
| `code/tiny-agent/full/` | `python3 check_agent.py` | `14 of 14 passed` |

`python3 tiny_agent.py` prints a trace for each question. `python3 real_model.py` calls a real provider and needs the reader's API key. Don't run it without the reader's say-so, since it costs money.

The book was written against the tag `book-edition-1`. Check it out if results don't match.

## Related repositories

The interactive exercises live in [AI-Builder-Lab](https://github.com/deepak-mukunthu/AI-Builder-Lab), which has its own `AGENTS.md` with the expected numbers. The other projects are listed in `docs/projects.md`.

## Helping a reader

- Find the reader's path first. A product manager wants the templates and the questions to ask. A developer wants the tiny agent. A builder wants the Sandbox and the Northwind pack.
- `docs/chapter-guide.md` gives the expected result for every chapter. Use it to check a reader's work.
- The exercises are meant to be solved. Point to the trace, the part, or the template row before giving the answer. Give the answer if they ask for it outright.
- When filling in a template for a reader's real product, ask them for the facts. Don't invent their users, data, limits or numbers.
- Don't reproduce or summarize book chapters that aren't in this repository. Refer the reader to the chapter by number.
- All companies, policies, orders and prices in the examples are fictional.

## Changing the code

- Keep the tiny agent free of third-party packages, and keep the code lines short enough to print in the book.
- After a change, run all three checks above and report the counts.
- Templates are Markdown and meant to be copied. Keep them plain, with no tool-specific syntax.
