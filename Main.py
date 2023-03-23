from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount

def main():
    #Creates an object from the CheckingAccount class and tests its methods and attributes
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

    #Creates an object from the SavingsAccount class and tests its methods and attributes
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