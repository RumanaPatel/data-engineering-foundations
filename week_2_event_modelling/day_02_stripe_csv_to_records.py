import csv

events = []

with open("data-engineering-foundations/week_2_event_modelling/data/stripe_balance_transactions.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        event = {
            "id": row["id"],
            "type": row["type"],
            "amount": int(row["amount"]),
            "currency": row["currency"]
        }

        events.append(event)

print(events)

# Validation step - printed total should be 0
total = 0

for event in events:
    total += event["amount"]

print("Net balance: ", total)