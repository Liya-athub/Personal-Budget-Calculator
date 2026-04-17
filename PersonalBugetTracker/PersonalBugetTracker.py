
def budget_calculator():
    print("=== Monthly Budget Calculator ===")

    income = float(input("Enter your monthly income: "))
    expenses = []
    total_expenses = 0

    while True:
        category = input("Enter expense category (or type 'done'):" ).strip()

        if category.lower() == "done":
            break

        amount = float(input(f"Enter amount for " + category + ":").strip())
        
        expenses.append((category, amount))
        total_expenses += amount

    remaining = income - total_expenses

    print("\n--- Budget Summary ---")
    print(f"Income: ${income:.2f}")
    print("Expenses:")
    for category, amount in expenses:
        print(f"{category}: ${amount:.2f}")

    print(f"\nTotal Expenses: ${total_expenses:.2f}")
    print(f"Remaining Balance: ${remaining:.2f}")

    if remaining < 0:
        print("Warning: You are over budget.")
    else:
        print("Great! You are within budget.")

budget_calculator()
