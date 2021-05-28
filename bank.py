class Bank:
   
    def __init__(self,balance,accountNumber,accountName):
        self.balance=balance
        self.accountNumber=accountNumber
        self.accountName=accountName
    def deposit(self):
        return f"Hello your balance amount is{self.balance}"
    def withdraw(self):
        return f"Hello this accountNumber {self.accountNumber} is allowed to withdraw"

    def transfer(self,newBalance):
        self.newBalance=newBalance
        return f"Hello this accountNumber{self.accountNumber} that has accountName{self.accountName} has transfered money successfully and the newBalance is{self.newBalance}"

        