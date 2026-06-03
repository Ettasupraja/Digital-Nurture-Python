def add_expense():
    expenses = [1000, 1500, 2000]
    new_expense = 500

    if new_expense <= 0:
        print("Invalid Expense")
        return

    expenses.append(new_expense)
    print("Updated Expenses:", expenses)

add_expense()