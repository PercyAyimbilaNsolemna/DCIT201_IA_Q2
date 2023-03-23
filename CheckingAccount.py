from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self):
        self.transaction_fee = 0
        super()

    #Creates  an __str__ method 
    def __str__(self):
        return "This is Checking Account class"

    #Creates a withdraw method that implements the withdraw abstract method in the BankAccount class
    def withdraw(self, amount):
        self.amount = amount
        self.transaction_fee = self.amount * 0.5
        self.balance = self.balance - self.transaction_fee

    #Created a deposit method that fully implements the abstract method in the BankAccount class
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount

    #Creates a setter and getter for the transaction fee
    @property
    def transaction_fee(self):
        return self._transaction_fee

    @transaction_fee.setter
    def transaction_fee(self, transaction_fee):
        self._transaction_fee = transaction_fee

    #Creates a getter and setter methods  for the amount attribute
    @property 
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount


def main():
    checkingAccount = CheckingAccount()

    print(checkingAccount)

    checkingAccount.owner = "Percy"
    print(checkingAccount.owner)

    checkingAccount.balance = 3000
    print(f"Balance: ${checkingAccount.balance}")

    checkingAccount.withdraw(100)
    print(f"Current Balance: ${checkingAccount.balance}")

    checkingAccount.deposit(50)
    print(f"Current Balance: ${checkingAccount.balance}")


if __name__ == "__main__":
    main()