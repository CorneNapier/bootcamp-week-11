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
    menuChoices = read_file("ExpenseTracker/menu.txt")
      
    while option not in optionsList:
        print(menuChoices)
        
        option = input("Enter an option from the menu choices above: ")
        
        if option not in optionsList:
            print(f'{option} is not a valid choice!!!')
    return option

def add_expense(expenses, name, amount, category):
    expenses.append({"name": name, "amount": amount, "category": category})

def get_total_expenses(expenses):
    return sum(expense["amount"] for expense in expenses)

def get_expenses_by_category(expenses, category):
    return [expense for expense in expenses if expense["category"] == category]

def main():
    expenses = []

    while True:
        mainMenu = expense_menu()

        if mainMenu == '1':
            name = input("Enter expense name: ")
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            add_expense(expenses, name, amount, category)
            print("Expense added successfully!")
        elif mainMenu == '2':
            total_expenses = get_total_expenses(expenses)
            print(f"Total Expenses: ${total_expenses}")
        elif mainMenu == '3':
            category = input("Enter category to view expenses: ")
            category_expenses = get_expenses_by_category(expenses, category)
            total_category_expenses = sum(expense["amount"] for expense in category_expenses)
            print(f"Total Expenses in {category}: ${total_category_expenses}")
            for expense in category_expenses:
                print(f"{expense['name']}: ${expense['amount']}")
        elif mainMenu == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()