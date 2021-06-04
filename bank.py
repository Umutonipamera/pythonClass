class Account:
   
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0
        self.transaction_fee=20  
        self.loan=0
        self.loan_limit=50000
    def deposit(self,amount): 
        if amount<=0:
            print ("Please deposit a valid amount")
        else:
            self.balance+=amount
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
               

            

         