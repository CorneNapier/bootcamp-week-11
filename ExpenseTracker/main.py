import tkinter as tk
from tkinter import messagebox, simpledialog
import tkinter.ttk as ttk
import tracker  
from Database.connect import *  

class ExpenseTrackerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Expense Tracker')

        # Setup a basic GUI layout with buttons to call your functions
        self.setup_gui()

    def setup_gui(self):
        # Add Expense Button
        self.add_expense_btn = tk.Button(self.master, text="Add Expense", command=self.add_expense)
        self.add_expense_btn.pack(pady=5)

        # View Expenses Button
        self.view_expenses_btn = tk.Button(self.master, text="View All Expenses", command=self.view_expenses)
        self.view_expenses_btn.pack(pady=5)

        # Remove Expense Button
        self.remove_expense_btn = tk.Button(self.master, text="Remove Expense", command=self.remove_expense)
        self.remove_expense_btn.pack(pady=5)

        # View Expenses by Category Button
        self.view_category_btn = tk.Button(self.master, text="View Expenses by Category", command=self.view_category_expenses)
        self.view_category_btn.pack(pady=5)

        # View Total Expenses Button
        self.view_total_btn = tk.Button(self.master, text="View Total Expenses", command=self.view_total_expenses)
        self.view_total_btn.pack(pady=5)

        # Exit Button
        self.exit_btn = tk.Button(self.master, text="Exit", command=self.master.quit)
        self.exit_btn.pack(pady=5)

    def add_expense(self):
        # Function to prompt user for expense details and add it
        expense_name = simpledialog.askstring("Input", "Enter expense name:")
        amount = simpledialog.askfloat("Input", "Enter expense amount:")
        expense_category = simpledialog.askstring("Input", "Enter expense category:")

        if expense_name and amount and expense_category:
            tracker.add_expense(expense_name, amount, expense_category)
            messagebox.showinfo("Success", "Expense added successfully.")

    def view_expenses(self):
        expenses = tracker.showAllExpenses()

        # Create a new window
        expense_window = tk.Toplevel(self.master)
        expense_window.title("All Expenses")

        # Define Treeview
        columns = ('ID', 'Name', 'Amount', 'Category')
        expense_tree = ttk.Treeview(expense_window, columns=columns, show='headings')

        # Define headings
        for col in columns:
            expense_tree.heading(col, text=col)

        # Add data to the treeview
        for expense in expenses:
            expense_tree.insert('', tk.END, values=expense)

        expense_tree.pack(expand=True, fill='both')

    def remove_expense(self):
     expense_id = simpledialog.askinteger("Input", "Enter the ID of the expense to be deleted:")
     if expense_id is not None:
        # Execute the SQL query to select the expense by ID
        dbCursor.execute("SELECT * FROM expenses WHERE ID = ?", (expense_id,))
        row = dbCursor.fetchone()
        if row is None:
            messagebox.showerror("Error", f"Delete not possible: No record with the ID {expense_id} exists.")
        else:
            # Execute the SQL query to delete the expense
            dbCursor.execute("DELETE FROM expenses WHERE ID = ?", (expense_id,))
            dbCon.commit()
            messagebox.showinfo("Success", f"The expense with the ID {expense_id} has been deleted.")

    def view_category_expenses(self):
        category = simpledialog.askstring("Input", "Enter the category to view expenses:")
        if category:
            category_expenses = tracker.get_expenses_by_category(category)
            if category_expenses:
                category_window = tk.Toplevel(self.master)
                category_window.title(f"Expenses in Category: {category}")

                # Define Treeview
                columns = ('ID', 'Name', 'Amount', 'Category')
                expense_tree = ttk.Treeview(category_window, columns=columns, show='headings')

                # Define headings
                for col in columns:
                    expense_tree.heading(col, text=col)

                # Add data to the treeview
                for expense in category_expenses:
                    expense_tree.insert('', tk.END, values=expense)

                expense_tree.pack(expand=True, fill='both')
            else:
                messagebox.showinfo("Info", f"No expenses found in category: {category}")

    def view_total_expenses(self):
        total = tracker.get_total_expenses()
        messagebox.showinfo("Total Expenses", f"Total Expenses: ${total}")

def main():
    root = tk.Tk()
    app = ExpenseTrackerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
