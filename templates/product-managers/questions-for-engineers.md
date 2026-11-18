# Questions to ask your engineers

- **Context.** What exactly does the model see on each call? Can you show me the full text for one real conversation?
- **Context.** Where do the documents come from, and what happens when one changes or is deleted?
- **Memory.** What do we remember about a user, for how long, and how do they delete it?
- **Tools.** Which systems can it read, and which can it change? Whose permissions does it use?
- **Rules.** Which of our "must never" rules are enforced in code, and which are only in the prompt?
- **Tests.** How many test cases do we have, who wrote them, and what's the pass rate today?
- **Tests.** When we change something, how soon do we know if it got worse?
- **Failures.** What did it get wrong this week, and what did we change because of it?
- **Cost.** What does one conversation cost, and what would a busy day cost?
- **Models.** What happens to our results if the provider updates or retires the model?
- **Exit.** How do we turn it off, and how fast?
