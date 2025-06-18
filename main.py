def personal_budget():
    print("=== Personal Monthly Budget Tracker ===")
    
    # Input income
    income = float(input("Enter your monthly income (QAR): "))
    
    # Input expenses
    print("\nEnter your monthly expenses:")
    rent = float(input(" - Rent: "))
    utilities = float(input(" - Utilities (water, electricity, internet): "))
    groceries = float(input(" - Groceries: "))
    transportation = float(input(" - Transportation: "))
    others = float(input(" - Other expenses: "))
    
    # Input savings
    savings = float(input("\nEnter your monthly savings (QAR): "))

    # Calculate totals
    total_expenses = rent + utilities + groceries + transportation + others
    remaining_balance = income - (total_expenses + savings)

    # Display summary
    print("\n=== Budget Summary ===")
    print(f"Monthly Income     : QAR {income:.2f}")
    print(f"Total Expenses     : QAR {total_expenses:.2f}")
    print(f"Savings            : QAR {savings:.2f}")
    print(f"Remaining Balance  : QAR {remaining_balance:.2f}")

    # Tips
    if remaining_balance < 0:
        print("⚠️  You are overspending. Try to reduce expenses or increase income.")
    elif remaining_balance < (0.1 * income):
        print("💡 Warning: You are saving less than 10% of your income.")
    else:
        print("✅ Good job! You're managing your budget well.")

# Run the budget tracker
personal_budget()
