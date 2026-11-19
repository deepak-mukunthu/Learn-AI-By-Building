# test_real_model.py: checks real_model.py offline.
# A fake "anthropic" module replays canned replies,
# so this needs no API key and costs nothing.
import sys
import types

class Block:
    def __init__(self, **kw):
        self.__dict__.update(kw)
    def model_dump(self, exclude_none=False):
        return dict(self.__dict__)

def reply(*blocks, stop="end_turn"):
    return types.SimpleNamespace(
        content=list(blocks), stop_reason=stop)

SENT = []   # every request real_model made
QUEUE = []  # replies to hand back, in order

class Messages:
    def create(self, **kw):
        SENT.append(kw)
        return QUEUE.pop(0)

fake = types.ModuleType("anthropic")
fake.Anthropic = lambda: types.SimpleNamespace(
    messages=Messages())
sys.modules["anthropic"] = fake

from real_model import real_model, run_turn, TOOLS

THINK = Block(type="thinking", thinking="...",
              signature="sig")
def text(t):
    return Block(type="text", text=t)
def use(name, **args):
    return Block(type="tool_use", id="tu_1",
                 name=name, input=args)

def check(label, ok):
    print("PASS" if ok else "FAIL", "|", label)
    return ok

results = []
msgs = [{"role": "system", "content": "SYS + note"},
        {"role": "user", "content": "hi"}]

QUEUE[:] = [reply(text("Hello."))]
results.append(check("text only",
    real_model(msgs) == {"answer": "Hello."}))
results.append(check("sends this turn's system",
    SENT[-1]["system"] == "SYS + note"))
names = {t["name"] for t in SENT[-1]["tools"]}
results.append(check("only tools that exist",
    names == set(TOOLS)))

QUEUE[:] = [reply(THINK, text("Hi there."))]
results.append(check("thinking, then text",
    real_model(msgs) == {"answer": "Hi there."}))

QUEUE[:] = [reply(THINK, stop="max_tokens")]
results.append(check("ran out of tokens",
    "person" in real_model(msgs)["answer"]))

SENT.clear()
QUEUE[:] = [reply(THINK, use("get_product",
                             sku="ECH-800")),
            reply(text("Out of stock, $129."))]
answer = run_turn("Is ECH-800 available?", "alex",
                  model=real_model)
second = SENT[1]["messages"]
kinds = [b["type"] for b in second[1]["content"]]
results.append(check("tool, then text",
    answer == "Out of stock, $129."))
results.append(check("thinking sent back",
    kinds == ["thinking", "tool_use"]))
results.append(check("result matches the call",
    second[2]["content"][0]["tool_use_id"] == "tu_1"))

print(f"{sum(results)} of {len(results)} passed")
sys.exit(0 if all(results) else 1)
