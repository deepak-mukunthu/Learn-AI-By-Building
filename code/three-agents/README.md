# Three agents, one loop

Chapter 2 of *Learn AI by Building* says every agent is the same five parts with different settings. This folder shows it in code. One loop, `agent_loop.py`, runs three agents. Each agent file holds only its settings.

| Part | `shop.py` (ShopBot) | `bank.py` (BankBot) | `helpdesk.py` (HelpDesk) |
| --- | --- | --- | --- |
| Context | `SYSTEM`: store questions only, never guess prices | `SYSTEM`: own accounts only, no financial advice | `SYSTEM`: IT questions only, never ask for a password |
| Data | `CATALOG`, `ORDERS` | `ACCOUNTS` | `EMPLOYEES`, `TICKETS`, `OUTAGES` |
| Tools | `get_product`, `get_order`, `refund` | `get_account`, `freeze_card`, `unfreeze_card` | `get_ticket`, `outage_status`, `reset_password` |
| Rules in code | Own orders only. Refunds within 30 days, and over $150 to a person | Own accounts only. Only a person may unfreeze a card | Identity verified before a reset. Executives' resets go to a person |
| Model | `ROUTES` and `answer()` stand in for the model | same | same |
| Harness | `run_turn()` in `agent_loop.py`, shared | shared | shared |

Memory is left out to keep the files short. Appendix D's checkpoints show how to add it to the tiny agent, and it goes in the same place here.

## Run it

```
cd code/three-agents
python3 agent_loop.py
python3 check_agents.py
```

Python 3 only, no packages, no network. `agent_loop.py` runs one question per agent and prints each trace. `check_agents.py` should print `15 of 15 passed`: four checks per agent on the words in the answer, plus one per agent on the action, such as "Sam's card stays frozen."

## Exercises

1. Run `diff shop.py bank.py`. Every line that differs is a setting. Nothing in the loop changes.
2. Add a fourth agent, for example a clinic's appointment assistant. Copy `bank.py`, change the settings, and add three cases to `check_agents.py`. You should not need to touch `agent_loop.py`.
3. Move one rule out of code and into the `SYSTEM` text only, for example delete the identity check in `reset_password`. Run the checks. The fake model ignores the sentence, as a real model sometimes does, and a check fails. That is why rules that matter live in code.

Everything here is invented: the store, the bank, the company, and their data.
