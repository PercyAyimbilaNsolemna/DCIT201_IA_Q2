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

    #Creates a getter and setter for the amount attribute
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        self._amount = amount

    #Creates a getter and setter for the difference attribute
    @property
    def difference(self):
        return self._difference

    @difference.setter
    def difference(self, difference):
        self._difference = difference

def main():
    savingsAccount = SavingsAccount()
    print(savingsAccount)

    savingsAccount.owner = "Sabastian Abelezele"
    print(f"Owner: {savingsAccount.owner}")

    savingsAccount.balance = 5000
    print(f"Balance: ${savingsAccount.balance}")

    savingsAccount.withdraw(1000)
    print(f"Dear customer you have withdrawn an amount of ${savingsAccount.amount}. Your current balance is {savingsAccount.balance}")

    savingsAccount.deposit(3000)
    print(f"Dear customer you have deposited an amount of ${savingsAccount.amount}. Your current balance is {savingsAccount.balance}")

    """""
    #This test tries to check if the account user tries to withdraw an amount more than the amount in his account
    savingsAccount.withdraw(10000)
    print(savingsAccount.balance)

    """

if __name__ == "__main__":
    main()