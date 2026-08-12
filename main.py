from finance_manager import FinanceManager


def main():
    manager = FinanceManager()

    while True:
        print("\n===== SMART BUDGET MANAGER =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Summary")
        print("5. Exit")

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
            print("Thank you for using Smart Budget Manager!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()