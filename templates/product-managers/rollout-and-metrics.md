# Staged rollout and metrics

## Rollout stages

| Stage | Who sees it | A person checks | Move on when |
| --- | --- | --- | --- |
| 1 Shadow | No one. It runs behind the scenes on real requests. | Every answer, compared with what staff did | It matches or beats staff on the test set and on live traffic |
| 2 Suggest | Staff only, as drafts | Every draft before it goes out | Staff accept most drafts with few edits |
| 3 Limited | A small share of customers or one team | A sample, plus every flagged case | No "must never" failures and steady quality for several weeks |
| 4 Broad | Everyone, with an easy handoff to a person | A weekly sample and every complaint | Ongoing: quality, cost, and complaints stay inside the bars |

Write a stop condition for each stage before launch, such as "if two must-never failures happen in a week, go back a stage."

## Ladder of metrics

| Level | Question | Example measure |
| --- | --- | --- |
| Quality | Is it right? | Pass rate on the test set |
| Safety | Does it stay inside the rules? | Count of "must never" failures (target zero) |
| Use | Do people choose it? | Share of eligible users who use it each week |
| Outcome | Did the job get done? | Requests resolved without a person, reopened rate |
| Value | Is it worth it? | Cost per resolved request, time saved |
| Trust | Do they believe it? | Satisfaction, complaints, how often staff override it |

Pick one measure from each level.
