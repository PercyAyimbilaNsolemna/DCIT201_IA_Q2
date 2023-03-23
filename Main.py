from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount

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