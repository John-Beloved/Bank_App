from account import Account

class CurrentAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)
