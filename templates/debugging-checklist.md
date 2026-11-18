# Five-question debugging checklist

Ask in order for any wrong answer. Stop at the first "no."

1. **Context.** Was every fact needed for the right answer in the folder (what the model was shown)?
2. **Memory.** Did the agent have what the user already told it?
3. **Tools.** Did each tool run, succeed, and return current data?
4. **Harness.** Was every rule that applies checked in code?
5. **Model.** With the right folder, facts, and rules, did the model still get it wrong? Check temperature and instructions.

Switching to a new model is the last thing to try, not the first.
