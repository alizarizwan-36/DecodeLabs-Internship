 # Expense Tracker

# Initialize total before the loop
total_expense = 0

print("=== Expense Tracker ===\n")
print("Enter your expenses one by one.")
print("Type 'done' to finish.\n")

while True:
    expense = input("Enter expense amount (or 'done' to quit): ")

    # Sentinel value to stop the program
    if expense.lower() == "done":
        break

    try:
        # Convert input to a number
        amount = float(expense)

        # Add to running total
        total_expense += amount

        print(f"Expense Added: ${amount:.2f}")
        print(f"Current Total: ${total_expense:.2f}\n")

    except ValueError:
        print("Invalid input! Please enter a numeric value.\n")

# Display final total after loop ends
print("\n=== Expense Summary ===")
print(f"FINAL TOTAL: ${total_expense:.2f}")
print("Thank you for using the Expense Tracker!")