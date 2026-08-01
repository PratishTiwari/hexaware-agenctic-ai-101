# hybrid agent in autogen-agent-patterns
# Python rules + AssistantAgent = a hybrid agent that can reason and code

import time
from _agents import agent_step, get_client, run

POLICY = "Hex Retail Accepts audio returns within 21 days of delivery."

ORDERS = {
    "AR-90455": {"days": 12, "faulty": True, "item": "Hex Studio Headphones"},
    "AR-90456": {"days": 34, "faulty": False, "item": "Hex Studio Buds Mk II"},
    "AR-90457": {"days": 5, "faulty": False, "item": "Hex Studio Headphones"},
    "AR-90458": {"days": 40, "faulty": True, "item": "Hex Studio Buds Mk II"},
}

TICKETS = [
    ("AR-90455", "Left earbud stopped working. Want to send it back"),
    ("AR-90456", "Changed my mind, want to return the headphones"),
    ("AR-90457", "Wrong color, please refund my order"),
    ("AR-90458", "These are faulty and I am well outside 21 days - where do I stand?"),
    ("AR-99999", "Please refund my order"),
    ("AR-90455", "My daughter dropped the headphones in water, can I return them?")
]

# an autogen agent will be called only when the rules give up.
JUDGEMENT = (
    "You are Hex Retail's senior returns adjudicator."
    f"{POLICY} Faulty good are additionally covered by a two-year warranty. "
    "You handle only the cases the rules could not settle. "
    "Reply in at most two sentences: the decision, then the reason."
)
