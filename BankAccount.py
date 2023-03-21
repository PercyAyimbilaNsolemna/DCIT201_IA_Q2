
class BankAccount:
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

    