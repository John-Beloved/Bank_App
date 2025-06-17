class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = amount + self.balance
        print(f"You have deposited: + {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(self.balance)
        else:
            print("Insufficient funds")




