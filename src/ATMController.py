class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def seeBalance(self):
        # print("The balance is {} dollers.".format(self.balance))
        return self.balance

    def withdraw(self, amount):
        # print("{} dollers has been withdrawn.".format(amount))
        self.balance -= amount

    def deposit(self, amount):
        # print("{} dollers has been deposited.".format(amount))
        self.balance += amount


class User:
    def __init__(self, name, pin, account):
        self.name = name
        self.pin = pin
        self.account = account
