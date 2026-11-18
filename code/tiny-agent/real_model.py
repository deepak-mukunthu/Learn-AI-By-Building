# real_model.py: swap the fake model for a real one.
# Needs: pip install anthropic, and an API key in
# the ANTHROPIC_API_KEY environment variable.
import json
import anthropic
from tiny_agent import run_turn, SYSTEM

client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"  # a small, cheap model

def tool(name, desc, **fields):
    return {"name": name, "description": desc,
            "input_schema": {
                "type": "object",
                "properties": fields,
                "required": list(fields)}}

TEXT = {"type": "string"}
TOOL_SPECS = [
    tool("get_product", "Price and stock for a "
         "product, by SKU like ECH-800", sku=TEXT),
    tool("get_order", "Status of one of this "
         "customer's orders, by ID like ORD-9001",
         order_id=TEXT),
    tool("refund", "Refund an order in full. "
         "Rules are checked in code.",
         order_id=TEXT),
]

def to_api(messages):
    """Our simple message list -> the API's format."""
    out, last_id = [], None
    for m in messages[1:]:  # [0] is the system
        if m["role"] == "user":
            out.append({"role": "user",
                        "content": m["content"]})
        elif m["role"] == "assistant":
            r = json.loads(m["content"])
            last_id = r["id"]
            out.append({"role": "assistant",
                        "content": [{
                            "type": "tool_use",
                            "id": r["id"],
                            "name": r["tool"],
                            "input": r["args"]}]})
        else:  # a tool result
            out.append({"role": "user",
                        "content": [{
                            "type": "tool_result",
                            "tool_use_id": last_id,
                            "content": m["content"]}]})
    return out

def real_model(messages):
    r = client.messages.create(
        model=MODEL, max_tokens=300,
        system=SYSTEM, tools=TOOL_SPECS,
        messages=to_api(messages))
    for block in r.content:
        if block.type == "tool_use":
            return {"tool": block.name,
                    "args": block.input,
                    "id": block.id}
    return {"answer": r.content[0].text}

if __name__ == "__main__":
    q = "Is ECH-800 available?"
    print(run_turn(q, "alex", model=real_model))
