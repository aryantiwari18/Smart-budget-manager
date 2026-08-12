import json
import os


class BudgetManager:

    def __init__(self):
        self.data_file = "budgets.json"
        self.budgets = self.load_budgets()

    def load_budgets(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                return {}

        return {}

    def save_budgets(self):
        with open(self.data_file, "w") as file:
            json.dump(self.budgets, file, indent=4)

    def set_budget(self):
        category = input("Enter budget category: ").strip().lower()

        try:
            amount = float(input("Enter budget amount: "))

            if amount <= 0:
                print("Budget must be greater than zero.")
                return

            self.budgets[category] = amount
            self.save_budgets()

            print(f"Budget set successfully for {category.title()}.")

        except ValueError:
            print("Please enter a valid amount.")

    def view_budgets(self):
        if not self.budgets:
            print("No budgets have been set.")
            return

        print("\n===== BUDGETS =====")

        for category, amount in self.budgets.items():
            print(f"{category.title()} : ₹{amount:.2f}")

    def check_budget(self, category, spent):
        category = category.lower()

        if category not in self.budgets:
            return

        budget = self.budgets[category]

        if spent > budget:
            print(
                f"⚠️ Budget exceeded for {category.title()}!"
            )

        elif spent >= budget * 0.8:
            print(
                f"⚠️ Warning: You have used "
                f"{(spent / budget) * 100:.1f}% of your "
                f"{category.title()} budget."
            )