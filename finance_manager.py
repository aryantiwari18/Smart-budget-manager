import json
import os
from datetime import datetime


class FinanceManager:

    def __init__(self):
        self.data_file = "transactions.json"
        self.budget_file = "budgets.json"
        self.transactions = self.load_data()
        self.budgets = self.load_budgets()

    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                return []

        return []

    def load_budgets(self):
        if os.path.exists(self.budget_file):
            try:
                with open(self.budget_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                return {}

        return {}

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump(self.transactions, file, indent=4)

    def add_income(self):
        amount = self.get_amount("Enter income amount: ")
        source = input("Enter income source: ").strip()

        transaction = {
            "type": "income",
            "amount": amount,
            "category": source,
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        self.transactions.append(transaction)
        self.save_data()

        print("Income added successfully.")

    def add_expense(self):
        amount = self.get_amount("Enter expense amount: ")
        category = input("Enter expense category: ").strip().lower()

        transaction = {
            "type": "expense",
            "amount": amount,
            "category": category,
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        self.transactions.append(transaction)
        self.save_data()

        print("Expense added successfully.")

        self.check_budget(category)

    def check_budget(self, category):
        if category not in self.budgets:
            return

        budget = self.budgets[category]

        spent = sum(
            transaction["amount"]
            for transaction in self.transactions
            if transaction["type"] == "expense"
            and transaction["category"].lower() == category
        )

        remaining = budget - spent

        print(f"\nBudget for {category.title()}: ₹{budget:.2f}")
        print(f"Spent: ₹{spent:.2f}")
        print(f"Remaining: ₹{remaining:.2f}")

        if spent > budget:
            print("⚠️ ALERT: Budget exceeded!")

        elif spent >= budget * 0.8:
            percentage = (spent / budget) * 100
            print(f"⚠️ WARNING: {percentage:.1f}% of your budget has been used.")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions found.")
            return

        print("\n===== TRANSACTIONS =====")

        for i, transaction in enumerate(self.transactions, start=1):
            print(
                f"{i}. {transaction['date']} | "
                f"{transaction['type'].upper()} | "
                f"₹{transaction['amount']:.2f} | "
                f"{transaction['category']}"
            )
    def search_expenses(self):
        category = input("Enter category to search: ").strip().lower()

        found = False

        print(f"\n===== EXPENSES: {category.title()} =====")

        for transaction in self.transactions:
            if (
                transaction["type"] == "expense"
                and transaction["category"].lower() == category
            ):
                print(
                    f"{transaction['date']} | "
                    f"₹{transaction['amount']:.2f} | "
                    f"{transaction['category']}"
                )
                found = True

        if not found:
            print("No expenses found for this category.")
    def show_summary(self):
        income = sum(
            transaction["amount"]
            for transaction in self.transactions
            if transaction["type"] == "income"
        )

        expenses = sum(
            transaction["amount"]
            for transaction in self.transactions
            if transaction["type"] == "expense"
        )

        balance = income - expenses

        print("\n===== FINANCIAL SUMMARY =====")
        print(f"Total Income   : ₹{income:.2f}")
        print(f"Total Expenses : ₹{expenses:.2f}")
        print(f"Balance        : ₹{balance:.2f}")

    def get_amount(self, message):
        while True:
            try:
                amount = float(input(message))

                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue

                return amount

            except ValueError:
                print("Please enter a valid number.")
    def monthly_summary(self):
        monthly_expenses = {}

        for transaction in self.transactions:
            if transaction["type"] == "expense":
                month = transaction["date"][:7]

                if month not in monthly_expenses:
                    monthly_expenses[month] = 0

                monthly_expenses[month] += transaction["amount"]

        if not monthly_expenses:
            print("No expenses available for monthly analysis.")
            return

        print("\n===== MONTHLY SPENDING =====")

        for month, amount in sorted(monthly_expenses.items()):
            print(f"{month} : ₹{amount:.2f}")
    def category_summary(self):
        category_expenses = {}

        for transaction in self.transactions:
            if transaction["type"] == "expense":
                category = transaction["category"]

                if category not in category_expenses:
                    category_expenses[category] = 0

                category_expenses[category] += transaction["amount"]

        if not category_expenses:
            print("No expenses available for category analysis.")
            return

        print("\n===== CATEGORY SPENDING =====")

        for category, amount in sorted(
            category_expenses.items(),
            key=lambda item: item[1],
            reverse=True
        ):
            print(f"{category.title()} : ₹{amount:.2f}")