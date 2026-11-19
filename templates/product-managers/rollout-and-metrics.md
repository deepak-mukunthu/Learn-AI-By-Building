# Staged rollout and metrics

## Rollout stages

| Stage | Who sees it | A person checks | Move on when |
| --- | --- | --- | --- |
| 1 · Shadow | No one. It runs behind the scenes on real requests. | Every answer, compared with what staff did | It matches or beats staff on the test set and on live traffic |
| 2 · Suggest | Staff only, as drafts | Every draft before it goes out | Staff accept most drafts with few edits |
| 3 · Limited | A small share of customers or one team | A sample, plus every flagged case | No "must never" failures and steady quality for several weeks |
| 4 · Broad | Everyone, with an easy handoff to a person | A weekly sample and every complaint | Ongoing: quality, cost, and complaints stay inside the bars |

Each stage needs two written stop conditions, decided before launch, when no one is emotionally invested.

- **Critical incidents stop things at once.** A single "must never" failure, such as a refund paid without approval, one customer shown another's data, or a harmful answer, pauses the affected capability the same day. Someone named in advance investigates. It comes back only after the cause is fixed and a test for it has been added.
- **Lower-severity errors use a rolling threshold.** Examples are wrong but harmless answers, unneeded handoffs, and a poor tone. Set a rate over a window, such as "more than 3% of sampled answers wrong over any 7 days," and go back a stage when it's crossed.

Don't put critical incidents on a counting rule. "Two in a week" means the first one is allowed.

## Ladder of metrics

| Level | Question | Example measure |
| --- | --- | --- |
| Quality | Is it right? | Pass rate on the test set |
| Safety | Does it stay inside the rules? | Count of "must never" failures (target zero) |
| Use | Do people choose it? | Share of eligible users who use it each week |
| Outcome | Did the job get done? | Requests resolved without a person, and reopened rates |
| Value | Is it worth it? | Cost per resolved request, time saved |
| Trust | Do they believe it? | Satisfaction scores, complaints, how often staff override it |

Pick one measure from each level. A product measured only on quality can be accurate and unused. One measured only on use can be popular and wrong.
