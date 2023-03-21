from abc import ABC, abstractmethod
class BankAccount(ABC):
    #Creates an initialization method
    def __init__(self, owner=None, balance=None):
        self.owner = owner
        self.balance = balance

    #Creates an __str__ which makes it possible to pass the object created from the class to the print function
    def __str__(self):
        return "This is a Bank Account class"

    #Creates a getter and setter for the owner attribute
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = owner

    #Creates a getter and setter methods for the balance attribute
    @property 
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    #Creates an abstract method called deposit
    @abstractmethod
    def deposit(self):
        pass

    #Creates an abstract method called withdraw
@abstractmethod
def withdraw(self):
    pass

def main():
    pass

if __name__ == "__main__":
    main()
   