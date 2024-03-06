from Database.connect import *
def read_file(file_path):
    try:
        with open(file_path) as readFile:
            rf = readFile.read()
            return rf
    except FileNotFoundError as nf:
        print(f'File not found because: {nf}')

def expense_menu():
    option = 0 
    optionsList = ['1', '2', '3', '4']
    menuChoices = read_file("ExpenseTracker/Text_Files/menu.txt")
      
    while option not in optionsList:
        print(menuChoices)
        
        option = input("Enter an option from the menu choices above: ")
        
        if option not in optionsList:
            print(f'{option} is not a valid choice!!!')
    return option

def add_expense(expenseName, amount, expenseCategory):
    dbCursor.execute("INSERT INTO expenses (expenseName, amount, expenseCategory) VALUES (?, ?, ?)", (expenseName, amount, expenseCategory))
    dbCon.commit()

def get_total_expenses():
    dbCursor.execute("SELECT SUM(amount) FROM expenses")
    total_expenses = dbCursor.fetchone()[0]
    return total_expenses

def get_expenses_by_category(expenseCategory):
    dbCursor.execute("SELECT * FROM expenses WHERE expenseCategory=?", (expenseCategory,))
    category_expenses = dbCursor.fetchall()
    return category_expenses

def main():   
    while True:
        mainMenu = expense_menu()

        if mainMenu == '1':
            expenseName = input("Enter expense name: ")
            amount = float(input("Enter expense amount: "))
            expenseCategory = input("Enter expense category: ")
            add_expense(expenseName, amount, expenseCategory)
            print("Expense added successfully!")
        elif mainMenu == '2':
            total_expenses = get_total_expenses()
            print(f"Total Expenses: ${total_expenses}")
        elif mainMenu == '3':
            expenseCategory = input("Enter category to view expenses: ")
            category_expenses = get_expenses_by_category(expenseCategory)
            total_category_expenses = sum(expense[2] for expense in category_expenses)
            print(f"Total Expenses in {expenseCategory}: ${total_category_expenses}")
            for expense in category_expenses:
                print(f"{expense[1]}: ${expense[2]}")
        elif mainMenu == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()