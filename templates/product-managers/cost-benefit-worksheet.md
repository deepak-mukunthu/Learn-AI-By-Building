# Cost and benefit worksheet

Fill in your own numbers. The example column is invented and only shows the arithmetic.

The worksheet keeps two results apart: *capacity*, which is the staff time the assistant frees up, and *cash*, which is money that stops leaving the company. Freed hours save nothing unless someone acts on them. Finance will ask which one you mean.

| Line | How to get it | Example |
| --- | --- | --- |
| A · Requests per month | From your logs | 10,000 |
| B · Share the assistant resolves alone | From the pilot, not a guess | 40% |
| C · Minutes a person spends per request today | Time ten requests | 6 |
| D · Review and correction minutes per resolved request | Sampling, checking, fixing what it got wrong. Measure in the pilot. | 0.6 |
| E · Hours released per month | A × B × (C - D) ÷ 60 | 4,000 × 5.4 ÷ 60 = 360 |
| F · Cost per person-hour, fully loaded | Ask finance | $40 |
| G · Capacity value | E × F | $14,400 |
| H · Hours that become real savings | Overtime or contractor hours you'll actually cut, or a hire you won't make. Name the budget line. | 150 contractor hours |
| I · Hours redeployed | E - H, and the work they move to | 210, to the backlog of complex cases |
| J · Cash reduction | H × F | $6,000 |
| K · Model and tool cost per month | Cost per conversation × A | $0.04 × 10,000 = $400 |
| L · Build and upkeep, per month | People's time, spread over a year | $6,000 |
| M · Net, capacity view | G - K - L | $8,000 |
| N · Net, cash view | J - K - L | -$400 |

The example pays off in capacity and loses a little cash. That's a common result, and you can defend it if the 210 redeployed hours go to work the team values, such as clearing a backlog or answering faster. Say so plainly rather than presenting $14,400 as savings.

The $0.04 per conversation here assumes short, single-question conversations on a small model. Chapter 10's ShopBot example cost $0.19 because each conversation had several turns and long retrieved text, priced at a large model's rates. Use the figure from your own pilot.

Then stress-test the result. Halve B and double K and L. In the example, released hours fall to 180, capacity value to $7,200, and the capacity view to -$5,600. The case doesn't survive that. It depends on the pilot's 40% holding up and on upkeep staying near $6,000. Before you commit, measure the assumption you're least sure of. Here, that's B, which came from a short pilot.
