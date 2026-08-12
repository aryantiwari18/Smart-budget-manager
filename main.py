from finance_manager import FinanceManager
from budget_manager import BudgetManager


def main():
    manager = FinanceManager()
    budget_manager = BudgetManager()

    while True:
        print("\n===== SMART BUDGET MANAGER =====")
        print("1. Add Income")
print("2. Add Expense")
print("3. View Transactions")
print("4. View Financial Summary")
print("5. Set Budget")
print("6. View Budgets")
print("7. Search Expenses")
print("8. Monthly Spending")
print("9. Category Spending")
print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_income()

        elif choice == "2":
            manager.add_expense()

        elif choice == "3":
            manager.view_transactions()

        elif choice == "4":
            manager.show_summary()

        elif choice == "5":
            budget_manager.set_budget()

        elif choice == "6":
            budget_manager.view_budgets()
        elif choice == "7":
            manager.search_expenses()

        elif choice == "8":
    manager.monthly_summary()

elif choice == "9":
    manager.category_summary()

elif choice == "10":
    print("Thank you for using Smart Budget Manager!")
    break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
            