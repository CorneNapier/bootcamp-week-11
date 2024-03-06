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

class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category
        
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        
    def add_expense(self, expense):
        self.expenses.append(expense)
    
    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)
    
    def expenses_category(self, category):
        return [expense for expense in self.expenses if expense.category == category]
    

        