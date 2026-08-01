import json
from _agents import run, agent_step, get_client

POLICY = ("Hex Retail accepts audio returns within 21 days of delivery. "
          "Faulty goods carry a two-year warranty. Change-of-mind returns cost "
          "GBP 3.95 postage; faulty returns are free.")

#  One sentence, four separate jobs hiding inside it.
REQUEST = ("My Hex Studio headphones arrived 12 days ago and the left earcup "
           "crackles. Can I return them, what will the postage cost me, how long "
           "does a refund take, and should I just get the Mk II instead?")

# Attempt 1. no plan, one agent, one shot, whatever it produces.
async def without_a_plan(client):
    """The obvious approach: just ask the agent to answer the request, and see what it produces."""
    return await agent_step(
        name="support",
        client=client,
        instruction=f"You are Hex Retail support. {POLICY} Be concise.",
        task=REQUEST)

# Attempt 2. plan first, the planner returns data
PLANNER = (
    "You are a planning agent. You will be given a request,"
    "and you will break it down into a numbered list of steps to answer it. "
    "Each step should be a single sentence, and should be actionable by a single agent. "
    "Do not answer the request yourself, just produce the plan."
)

def normalize(text: str) -> str:
    """Lowercase, and straigten the curly quotes models actually produce.
    Models write "isn't" with U+2019, not the ASCII apostrophe.
    They also use U+201C and U+201D for quotes, not the ASCII double quote.
    This function normalizes those characters to the ASCII versions, and lowercases the text.
    check that works and a check that silently always passes,
    so that we can see what the model produced without failing the test.
    """
    return text.lower().replace("\u2019", "'").replace("\u2018", "'")

REFUSALS = ("isn't provided", "is not provided", "i can't", "i cannot",
            "don't have", "do not have", "no information", "not able to",
            "isn't available", "is not available", "cannot answer", "can't answer",
            "not sure", "i'm not sure", "i am not sure", "i'm not able",
            "i am not able", "i'm unable", "i am unable",)