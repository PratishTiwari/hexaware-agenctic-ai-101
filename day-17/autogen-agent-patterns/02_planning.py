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


# Attempt 2. plan first, the planner returns data