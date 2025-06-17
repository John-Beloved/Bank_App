from account import Account


class SavingsAccount(Account):
    def __init__(self, balance, limit):
        Account.__init__(self, balance)
        self.limit = limit

    def deposit(self, amount):
        super().deposit(amount)

    def withdraw(self, amount):
        if amount <= self.balance - self.limit:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds respecting minimum balance limit.")
