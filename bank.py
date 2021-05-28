class Bank:
    accountType="Personal"
    def __init__(self,balance,accountNumber,accountName):
        self.balance=balance
        self.accountNumber=accountNumber
        self.accountName=accountName
    def deposit(self):
        return f"Hello your balance is{self.balance}, your accountNumber is{self.accountNumber}, and your accountName is{self.accountName}"
