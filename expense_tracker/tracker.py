from .models import Expense  # Importing the Expense class from the models module
from .database import Database  # Importing the Database class from the database module

class ExpenseTracker:
    def __init__(self):
        # Creating an instance of Database to interact with the database
        self.db = Database()

    def add_expense(self, name, amount):
        # Creating an instance of Expense with the provided name and amount
        expense = Expense(name, amount)
        # Adding the expense instance to the database
        self.db.add_expense(expense)

    def list_expenses(self):
        # Retrieving all expenses from the database
        expenses = self.db.get_expenses()
        # Iterating over each expense and printing its details
        for expense in expenses:
            print(f"{expense.name}: ${expense.amount}")

    def run(self):
        # Infinite loop to keep the program running until the user decides to exit
        while True:
            # Getting user input for the action to perform
            action = input("Enter 'add' to add an expense or 'list' to list expenses: ")
            if action == 'add':
                # Getting the name of the expense from the user
                name = input("Enter expense name: ")
                # Getting the amount of the expense from the user and converting it to float
                amount = float(input("Enter expense amount: "))
                # Adding the expense using the add_expense method
                self.add_expense(name, amount)
            elif action == 'list':
                # Listing all expenses using the list_expenses method
                self.list_expenses()
            else:
                # Handling invalid input by printing an error message
                print("Invalid action")
