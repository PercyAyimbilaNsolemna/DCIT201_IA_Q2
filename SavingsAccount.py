from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, difference=None):
        self.difference = difference
        super()

    #Creates an __str__ method that makes it possible for the object created to be passed to the print function
    def __str__(self):
        return "This is Savings Account class"

    #Creates an implementation for the withdraw abstract method in the BankAccount class
    def withdraw(self, amount):
        self.amount = amount 
        self.difference = self.balance - self.amount
        if self.difference >= 0:
            self.balance = self.difference
        else:
            raise ValueError("Dear customer you have insufficient balance to complete this transacion")

    #Creates an implementation for the deposit abstract method in the BankAccount class
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount

    
    
