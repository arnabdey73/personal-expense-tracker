from .models import Expense  # Importing the Expense class from the models module

class Database:
    def __init__(self):
        # Initializing an empty list to store expenses
        # This list will hold instances of the Expense class
        self.expenses = []

    def add_expense(self, expense: Expense):
        # Adding an expense to the list
        # The expense parameter is expected to be an instance of the Expense class
        self.expenses.append(expense)

    def get_expenses(self):
        # Returning the list of expenses
        # This method provides access to the stored expenses
        return self.expenses
