# real_model.py: swap the fake model for a real one.
# Needs: pip install anthropic, and an API key in
# the ANTHROPIC_API_KEY environment variable.
import json
import anthropic
from tiny_agent import run_turn, TOOLS

client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"  # a small, cheap model

def tool(name, desc, **fields):
    return {"name": name, "description": desc,
            "input_schema": {
                "type": "object",
                "properties": fields,
                "required": list(fields)}}

TEXT = {"type": "string"}
SPECS = [
    tool("get_product", "Price and stock for a "
         "product, by SKU like ECH-800", sku=TEXT),
    tool("get_order", "Status of one of this "
         "customer's orders, by ID like ORD-9001",
         order_id=TEXT),
    tool("refund", "Refund an order in full. "
         "Rules are checked in code.",
         order_id=TEXT),
    tool("search_policy", "Store policy passages "
         "that match a question", query=TEXT),
    tool("get_shipping", "Carrier and days to ship "
         "for one of this customer's orders",
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
                        "content": r["blocks"]})
        else:  # a tool result
            out.append({"role": "user",
                        "content": [{
                            "type": "tool_result",
                            "tool_use_id": last_id,
                            "content": m["content"]}]})
    return out

def real_model(messages):
    r = client.messages.create(
        model=MODEL, max_tokens=2000,
        system=messages[0]["content"],  # + notes
        tools=[s for s in SPECS if s["name"] in TOOLS],
        tool_choice={"type": "auto",  # one at a time
                     "disable_parallel_tool_use": True},
        messages=to_api(messages))
    if r.stop_reason == "max_tokens":
        return {"answer": "Sorry, I ran out of room. "
                "A person will help."}
    for block in r.content:
        if block.type == "tool_use":
            # Send every block back with the result,
            # thinking blocks included.
            blocks = [b.model_dump(exclude_none=True)
                      for b in r.content]
            return {"tool": block.name,
                    "args": dict(block.input),
                    "id": block.id, "blocks": blocks}
    # Answers may start with a thinking block, so
    # pick out the text blocks by type.
    text = "".join(b.text for b in r.content
                   if b.type == "text").strip()
    return {"answer": text or "Sorry, I have no "
            "answer. A person will help."}

if __name__ == "__main__":
    q = "Is ECH-800 available?"
    print(run_turn(q, "alex", model=real_model))
