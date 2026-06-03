import csv

expenses = {}

with open("expenses.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        category = row["category"]
        amount = float(row["amount"])

        expenses[category] = expenses.get(category, 0) + amount

print("Expense Summary")

for category, total in expenses.items():
    print(category, ":", total)