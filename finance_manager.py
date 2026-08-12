import json
import os
from datetime import datetime


class FinanceManager:

    def __init__(self):
        self.data_file = "transactions.json"
        self.transactions = self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                return []

        return []

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump(self.transactions, file, indent=4)

    def add_income(self):
        amount = self.get_amount("Enter income amount: ")
        source = input("Enter income source: ")

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
        category = input("Enter expense category: ")

        transaction = {
            "type": "expense",
            "amount": amount,
            "category": category,
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        self.transactions.append(transaction)
        self.save_data()

        print("Expense added successfully.")

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

    def show_summary(self):
        income = sum(
            t["amount"]
            for t in self.transactions
            if t["type"] == "income"
        )

        expenses = sum(
            t["amount"]
            for t in self.transactions
            if t["type"] == "expense"
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