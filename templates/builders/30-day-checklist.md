# Your first 30 days: day-by-day checklist

- [ ] **Days 1 to 2.** Choose the problem. Measure how it's handled today (volume, minutes per request, errors). *Done when:* you have three baseline numbers.
- [ ] **Days 3 to 4.** Fill in the job card and write ten test questions with expected answers. Show both to one person who will use the assistant. *Done when:* they say "yes, that's the job, and those are the right questions."
- [ ] **Days 5 to 7.** Check your platform against the list in Appendix G. Run the upload check, then gather and clean five documents. *Done when:* each has a title and a date, and none fails the check.
- [ ] **Days 8 to 10.** Write the instructions, build the first version, and run all ten tests. *Done when:* you have a first score.
- [ ] **Days 11 to 18.** Fix one failure a day, rerunning all ten each time. *Done when:* the four "must never" tests pass on every run, and the rest are steady.
- [ ] **Days 19 to 21.** Add five more tests from what you learned, mostly "not covered" and trick cases. Then check the gate before anyone else sees the assistant. *Gate:* zero unresolved critical failures across all 15 tests, run three times each. A good total doesn't count if any "must never" case failed. If one did, fix it and run the gate again before the pilot.
- [ ] **Days 22 to 25.** Pilot with three to five users. Read every conversation. *Done when:* you've read them all and logged each failure.
- [ ] **Days 26 to 28.** Fix the worst failures and add them as tests. *Done when:* no failure of the "must never" kind.
- [ ] **Days 29 to 30.** Compare to your baseline. Write one page: what worked, what didn't, what next. *Done when:* you can show numbers to your manager.

## Before you upload anything

Do this check before you choose or upload a single file.

- [ ] Is the document one you're allowed to share with this tool? Check your company's rules first.
- [ ] Does it contain personal details, such as names, salaries, or health information? If so, remove them or don't use it.
- [ ] Who can use this assistant, and can they see the files behind it? Some tools let users download the source documents.
- [ ] Does the platform use your files to train its models? Find the setting or the policy statement and write down what it says.
- [ ] How will you take the assistant down, and who will know it's been taken down?
- [ ] If it's flat-rate pricing, what are the monthly limits? What happens when a team reaches them?
