# agent_loop.py: one loop for any agent.
# The loop never changes. Each agent file (shop.py,
# bank.py, helpdesk.py) supplies only its settings:
# instructions, data, tools, rules, and replies.
import json
import re

def fake_model(agent, messages):
    """Stands in for a real model. Picks a tool from
    the agent's ROUTES, or writes the final answer
    from a tool result."""
    last = messages[-1]
    if last["role"] == "tool":
        return agent.answer(json.loads(last["content"]))
    text = last["content"]
    words = text.replace("?", " ").split()
    for pattern, keyword, tool, arg in agent.ROUTES:
        if keyword and keyword not in text.lower():
            continue
        if pattern is None:  # no id needed
            return {"tool": tool, "args": {}}
        for w in words:
            if re.fullmatch(pattern, w):
                return {"tool": tool, "args": {arg: w}}
    return {"answer": agent.FALLBACK}

def run_turn(agent, question, user, trace=None):
    """The harness. The same code for every agent."""
    messages = [{"role": "system",
                 "content": agent.SYSTEM},
                {"role": "user", "content": question}]
    for step in range(5):  # stop runaway loops
        reply = fake_model(agent, messages)
        if "answer" in reply:
            return reply["answer"]
        name, args = reply["tool"], reply["args"]
        args.pop("user", None)  # the model can't pick
        if name not in agent.TOOLS:
            result = {"error": f"unknown tool {name}"}
        elif name in agent.NEEDS_USER:
            result = agent.TOOLS[name](user=user,
                                       **args)
        else:
            result = agent.TOOLS[name](**args)
        print(f"  [trace] {name} {args} -> {result}")
        if trace is not None:
            trace.append((name, args, result))
        messages.append({"role": "assistant",
                         "content": json.dumps(reply)})
        messages.append({"role": "tool",
                         "content": json.dumps(result)})
    return "Sorry, I got stuck. A person will help."

if __name__ == "__main__":
    import bank, helpdesk, shop
    demo = [
        (shop, "sam", "Please refund ORD-9003"),
        (bank, "sam", "Unfreeze the card on ACC-1002"),
        (helpdesk, "lee", "Please reset my password"),
    ]
    for agent, user, q in demo:
        print(f"{agent.NAME} | {user}: {q}")
        print(f"  {run_turn(agent, q, user)}\n")
