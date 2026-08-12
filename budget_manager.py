class BudgetManager:

    def __init__(self):
        self.budgets = {}

    def set_budget(self):
        category = input("Enter budget category: ").strip()

        try:
            amount = float(input("Enter budget amount: "))

            if amount <= 0:
                print("Budget must be greater than zero.")
                return

            self.budgets[category.lower()] = amount
            print(f"Budget set successfully for {category}.")

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
                f"⚠️ Budget exceeded for {category.title()}! "
                f"Budget: ₹{budget:.2f}, Spent: ₹{spent:.2f}"
            )

        elif spent >= budget * 0.8:
            print(
                f"⚠️ Warning: You have used "
                f"{(spent / budget) * 100:.1f}% of your {category.title()} budget."
            )