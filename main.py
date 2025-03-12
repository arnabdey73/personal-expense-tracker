# Importing the ExpenseTracker class from the tracker module within the expense_tracker package
# This demonstrates the concept of importing specific classes from modules
from expense_tracker.tracker import ExpenseTracker

def main():
    # Creating an instance of ExpenseTracker
    # This demonstrates object instantiation in Python
    tracker = ExpenseTracker()
    
    # Running the main loop of the tracker
    # This demonstrates calling a method on an object
    tracker.run()

# The following condition checks if this script is executed directly (not imported as a module)
# If true, it calls the main function
# This demonstrates the use of the __name__ variable and the if __name__ == "__main__" idiom
if __name__ == "__main__":
    main()
