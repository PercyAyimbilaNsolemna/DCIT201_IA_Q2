from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self):
        super()

    #Creates an __str__ method that makes it possible for the object created to be passed to the print function
    def __str__(self):
        return "This is Savings Account class"

    