from collections import defaultdict
from datetime import datetime

# Sample data structure for transactions:
# Each transaction is a dict: 
# { "date": "YYYY-MM-DD", "type": "income" or "expense", "category": str, "amount": float }

transactions = [
    {"date": "2025-04-01", "type": "income", "category": "Salary", "amount": 3000.0},
    {"date": "2025-04-03", "type": "expense", "category": "Groceries", "amount": 150.5},
    {"date": "2025-04-15", "type": "expense", "category": "Transport", "amount": 60.0},
    {"date": "2025-05-01", "type": "income", "category": "Freelance", "amount": 1200.0},
    {"date": "2025-05-02", "type": "expense", "category": "Rent", "amount": 700.0},
]

def monthly_summary(transactions):
    summary = defaultdict(lambda: {"income": 0, "expense": 0})
    for t in transactions:
        dt = datetime.strptime(t["date"], "%Y-%m-%d")
        key = dt.strftime("%Y-%m")
        summary[key][t["type"]] += t["amount"]

    print("Monthly Summary:")
    for month, amounts in sorted(summary.items()):
        income = amounts["income"]
        expense = amounts["expense"]
        net = income - expense
        print(f"{month}: Income = ${income:.2f}, Expense = ${expense:.2f}, Net = ${net:.2f}")
    print()

def category_summary(transactions):
    summary = defaultdict(float)
    for t in transactions:
        key = (t["category"], t["type"])
        summary[key] += t["amount"]

    print("Category Summary:")
    categories = set(cat for cat, _ in summary.keys())
    for cat in sorted(categories):
        income = summary.get((cat, "income"), 0)
        expense = summary.get((cat, "expense"), 0)
        print(f"{cat}: Income = ${income:.2f}, Expense = ${expense:.2f}")
    print()

# Example usage:
monthly_summary(transactions)
category_summary(transactions)
