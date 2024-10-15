import json
import datetime
from datetime import timedelta

# Global variable for storing expenses
expenses = []

# Load expenses from file
def load_expenses(file_name='expenses.json'):
    try:
        with open(file_name, 'r') as file:
            global expenses
            expenses = json.load(file)
        print(f"Loaded {len(expenses)} previous expenses.")
    except FileNotFoundError:
        print("No previous data found, starting fresh.")

# Save expenses to file
def save_expenses(file_name='expenses.json'):
    with open(file_name, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense():
    amount = float(input("Enter amount: $"))
    category = input("Enter category (e.g., Food, Transport): ")
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = str(datetime.date.today())
    expense = {'amount': amount, 'category': category, 'date': date}
    expenses.append(expense)
    print("Expense added!")
    save_expenses()

# View total spending by category or overall
def view_summary():
    total_spent = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal overall spending: ${total_spent:.2f}")
    
    categories = {}
    for expense in expenses:
        category = expense['category']
        categories[category] = categories.get(category, 0) + expense['amount']
    
    print("\nSpending by category:")
    for category, total in categories.items():
        print(f"{category}: ${total:.2f}")
    
# View summary by time period
def view_summary_by_time():
    print("\n1. Daily Summary")
    print("2. Weekly Summary")
    print("3. Monthly Summary")
    choice = input("Choose an option: ")

    if choice == '1':
        group_by_time('daily')
    elif choice == '2':
        group_by_time('weekly')
    elif choice == '3':
        group_by_time('monthly')
    else:
        print("Invalid choice. Returning to menu.")

# Group expenses by time (daily, weekly, or monthly)
def group_by_time(period):
    now = datetime.date.today()
    
    if period == 'daily':
        time_limit = timedelta(days=1)
    elif period == 'weekly':
        time_limit = timedelta(weeks=1)
    elif period == 'monthly':
        time_limit = timedelta(days=30)

    filtered_expenses = [expense for expense in expenses if (now - datetime.datetime.strptime(expense['date'], "%Y-%m-%d").date()) <= time_limit]
    
    total_spent = sum(expense['amount'] for expense in filtered_expenses)
    print(f"\nTotal spending for the last {period}: ${total_spent:.2f}")
    
    categories = {}
    for expense in filtered_expenses:
        category = expense['category']
        categories[category] = categories.get(category, 0) + expense['amount']
    
    print(f"Spending by category in the last {period}:")
    for category, total in categories.items():
        print(f"{category}: ${total:.2f}")

# Delete an expense by index
def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return

    print("\nExpense List:")
    for idx, expense in enumerate(expenses):
        print(f"{idx + 1}. {expense['date']} - {expense['category']} - ${expense['amount']:.2f}")
    
    index = int(input("\nEnter the number of the expense to delete: ")) - 1
    if 0 <= index < len(expenses):
        del expenses[index]
        save_expenses()
        print("Expense deleted.")
    else:
        print("Invalid index.")

# Edit an expense by index
def edit_expense():
    if not expenses:
        print("No expenses to edit.")
        return

    print("\nExpense List:")
    for idx, expense in enumerate(expenses):
        print(f"{idx + 1}. {expense['date']} - {expense['category']} - ${expense['amount']:.2f}")
    
    index = int(input("\nEnter the number of the expense to edit: ")) - 1
    if 0 <= index < len(expenses):
        print("Editing expense...")
        new_amount = float(input(f"Enter new amount (current: ${expenses[index]['amount']:.2f}): ") or expenses[index]['amount'])
        new_category = input(f"Enter new category (current: {expenses[index]['category']}): ") or expenses[index]['category']
        new_date = input(f"Enter new date (current: {expenses[index]['date']}) or leave blank to keep it: ") or expenses[index]['date']
        
        expenses[index] = {'amount': new_amount, 'category': new_category, 'date': new_date}
        save_expenses()
        print("Expense updated.")
    else:
        print("Invalid index.")

# User menu
def menu():
    while True:
        print("\n1. Add an expense")
        print("2. View overall summary")
        print("3. View summary by time (Daily/Weekly/Monthly)")
        print("4. Delete an expense")
        print("5. Edit an expense")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            view_summary_by_time()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            edit_expense()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

# Main function
if __name__ == "__main__":
    load_expenses()
    menu()
