from tkinter import *
from tkinter import ttk
import pandas as pd
from pandastable import Table

# Variables
expense_row = 6
name_num = 1

# Window
root = Tk(screenName="Budget Tracker", baseName="Budget Tracker")
root.title("Budget Tracker")
frm = ttk.Frame(root, padding=10)
frm.grid()

# Budget
budget_amount = DoubleVar()

# Expenses
expenses = {"BUDGET": 0}
expense_name = StringVar()
expense_amount = DoubleVar()

# Functions
def display_expenses():
    global expense_row, expenses, name_num
    
    name = expense_name.get().strip()
    amount = expense_amount.get()
    
    if not name or amount <= 0:
        return
    
    key = name
    if name in expenses:
        key = f"{name}_{name_num}"    
        name_num += 1
        
    expenses[key] = amount
    
    row = expense_row + 1
    Label(frm, text=key).grid(row=(row), column=0)
    Label(frm, text=f"${expenses[key]}").grid(row=(row), column=1)
        
    expense_row += 1
    analyze_button.grid(row=expense_row + 2, column=7)

def analyze_expenses(expenses):   
    expenses["BUDGET"] = budget_amount.get()
    
    df = pd.DataFrame(list(expenses.items()), columns=["Name", "Amount"])
    
    total_expenses = df["Amount"][1:].sum()
    df.loc["Total Expenses"] = ["Total Expenses", total_expenses]
    
    df.loc["Budget Left"] = ["Budget Left", expenses["BUDGET"] - total_expenses]
    
    # Display Analysis
    new_window = Toplevel(root)
    new_window.title("Analysis")
    
    expense_table = Table(new_window, dataframe=df, showtoolbar=False, showstatusbar=False)
    
    expense_table.show()
    
    
# Title
Label(frm, text="Budget Tracker").grid(row=0, column=0)

# Budget
Label(frm, text="Budget:").grid(row=1, column=0)
budget_entry = Entry(frm, textvariable=budget_amount)
budget_entry.grid(row=1, column=1)

# Expenses
Label(frm, text="Add Expenses").grid(row=2, column=0)

# Expenses Name
Label(frm, text="Name:").grid(row=3, column=0)
ExpenseAmount_entry = Entry(frm, textvariable=expense_name)
ExpenseAmount_entry.grid(row=3, column=1)

# Expenses Amount
Label(frm, text="Amount:").grid(row=4, column=0)
ExpenseAmount_entry = Entry(frm, textvariable=expense_amount)
ExpenseAmount_entry.grid(row=4, column=1)

# Add Expenses
Button(frm, text="Add Expense", command=display_expenses).grid(row=5, column=4)
Label(frm, text="Expenses").grid(row=expense_row, column=0)

# Analyze The Expenses
analyze_button = Button(frm, text="Analyze", command=lambda:analyze_expenses(expenses))


if __name__ == "__main__":
    root.mainloop()