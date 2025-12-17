"""
Week 2 – Day 1
Stripe event modelling using dictionaries

Goal:
- Represent real-world payment events as structured data
- Use positive / negative amounts to reflect money moving in and out
- Validate the model using a simple balance check
"""

# Each dictionary represents ONE hypothetical real-world Stripe event
# Positive amounts add to the box
# Negative amounts remove from the box

charge_event = {
    "type": "charge",
    "amount": 5000
}

fee_event = {
    "type": "fee",
    "amount": -175 # stripe fee of £1.75
}

payout_event = {
    "type": "payout",
    "amount": -4825  # money sent to bank in pence (£50 - £1.75)
}

# A list of events represents a small dataset (like a CSV)
stripe_events = [
    charge_event,
    fee_event,
    payout_event
]

# Simple validation check:
# When all events are accounted for, balance should net to 0

total = 0

for event in stripe_events:
    total += event["amount"]

print(total)