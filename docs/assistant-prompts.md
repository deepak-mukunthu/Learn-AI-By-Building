# Prompts for your AI assistant

You can work through the book with a coding agent or a personal AI assistant at your side. These prompts are written for that. Copy one, fill in the brackets, and paste it in.

Both repositories have an `AGENTS.md` file that tells an assistant how to run the code, what numbers to expect, and to coach you rather than hand you the answers. Most coding agents read it on their own. For a chat assistant, give it the file or the link.

## Set up

> Clone https://github.com/deepak-mukunthu/Learn-AI-By-Building and https://github.com/deepak-mukunthu/AI-Builder-Lab, check out the tag `book-edition-1` in both, and read each `AGENTS.md`. Then run the checks it lists and tell me whether everything passes.

If your assistant can't run code, give it `llms.txt` from this repository instead. It lists every file with a link.

## Any reader

**Find the part that failed.**

> Here is a wrong answer from my assistant, and what I know about how it got there: [paste the question, the answer, and any trace or logs]. Walk me through `templates/debugging-checklist.md` one question at a time. Ask me for anything you can't see. Don't blame the model until the checklist has ruled out context, memory, tools, and the harness.

**Check my ShopBot progress.**

> I've applied [number] fixes in the AI Builder Lab and my quality score reads [score]. Run `node tools/report.js --fixes [number]` in AI-Builder-Lab and tell me whether my numbers match. If they don't, help me work out why. Then tell me which part the top open hotspot belongs to, but not the fix.

**Write test cases.**

> Using `templates/test-case-sheet.md`, help me write ten test cases for [my assistant and what it does]. Ask me about the questions real users send before you suggest any. Include at least two that should be refused or handed to a person.

## Product managers

**Fill in the spec.**

> Using `templates/product-managers/ai-feature-spec.md`, interview me one question at a time about [feature]. Fill in the spec from my answers. Don't invent users, data, limits, or numbers. Write "unknown" where I don't know, and list those at the end as questions to resolve.

**Prepare a design review.**

> Turn `templates/product-managers/questions-for-engineers.md` into an agenda for a 30-minute design review of [feature]. Put the questions most likely to change the launch decision first, and say what a good answer and a worrying answer would sound like for each.

**Check the business case.**

> Here is my filled-in `templates/product-managers/cost-benefit-worksheet.md`: [paste it]. Check the arithmetic, list every assumption, and tell me which one would change the answer most if it were wrong.

## Developers

**Read a trace.**

> In `code/tiny-agent`, run `python3 tiny_agent.py`. For the first question, label each line of the trace with the part it belongs to (model, context, memory, tools, harness) and explain in two sentences what the harness did.

**Add a tool.**

> Help me add a tool to `code/tiny-agent/tiny_agent.py` that [does something], and a test for it in `check_agent.py`. Don't use any packages. Let me write the code, and review it when I ask. Run the checks when I'm done.

**Try a real model.**

> Run `python3 test_real_model.py` in `code/tiny-agent` and confirm it passes. Then explain what `real_model.py` will send to the provider and roughly what one run costs, before I run it with my key.

## Builders

**Build the help desk.**

> I'm building the help-desk assistant on [platform]. Using `templates/builders/northwind-document-pack.md`, tell me how to load the documents and write the instructions there. Use `templates/system-prompt-skeleton.md` for the instructions.

**Grade it.**

> Here are my assistant's answers to the questions in `templates/builders/helpdesk-test-questions.md`: [paste them]. Mark each pass or fail against the good answer listed for it, and for each failure, name the part to look at first.

**Keep me on track.**

> I'm on day [number] of `templates/builders/30-day-checklist.md`. Show me today's task, ask me what I got done yesterday, and tell me if I'm falling behind.
