from datetime import datetime
class Account:
   
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0
        self.transaction_fee=20  
        self.loan=0
        self.loan_limit=50000
        self.transactions=[]
    def deposit(self,amount):
         
        if amount<=0:
            print ("Please deposit a valid amount")
        else:
            self.balance+=amount
            transaction={"amount":amount,"balance":self.balance,"narration":"you deposited","time":datetime.now()}
            self.transactions.append(transaction)
            return f"Hello {self.name} you have deposited {amount} your new balance is {self.balance}"

    def withdraw (self, withdraw_amount):  
         self.withdraw_amount=withdraw_amount
         total=withdraw_amount+self.transaction_fee
         if withdraw_amount<=0:
            return"input valid amount"
         elif total>self.balance:
            return "insuficient balance"
         else:
            self.balance - total
            return f"Hello {self.name} you can now borrow{self.withdraw_amount}"
    def borrow(self,amount):
        if amount>=self.loan_limit:
           return "you are not allowed to borrow"  
        elif amount<0:
            return "you can't borrow"   
            
        elif self.loan>0:
            return "You  have an existing loan"

        else:
            loan_fee=amount*0.05
            self.loan=amount+loan_fee
            self.balance+=amount
            return f"hello {self.name}.You have borrowed loan of  {amount},your new balance is {self.balance} and your loan balance is {self.loan}"
    def get_statement(self):   
        for transaction in self.transactions:
            amount=transaction["amount"] 
            narration=transaction["narration"]   
            balance=transaction["balance"] 
            time=transaction["time"]   
            date=time.strftime("%D")

            print(f"{date}....{narration}.... {amount}... balance{balance}....{date}")


    def repayment (self,amount):
        if amount<0: 
            return "enter valid amount"
        elif amount>self.loan:
            remainder=amount-self.loan
            self.balance+=remainder
            transaction={"amount":amount,"balance":self.balance,"narration":"repayment","time":datetime.now()}
            self.transactions.append(transaction)
            return f"Hello, you have repayed {amount} , your remainder{remainder} has been added to your {self.balance}"
        else: 
            self.balance+=amount  

            transaction={"amount":amount,"balance":self.balance,"narration":"you have repay","time":datetime.now()}
            self.transactions.append(transaction)
            return f"Hello, you have repayed {amount}, your new balance is{self.balance}"
            

             


            

         