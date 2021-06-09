from bank import Account
acc=Account("Pamela","0000")
print(acc.deposit(5000))
print(acc.deposit(200))
print(acc.deposit(300))
print(acc.withdraw (4000))
print(acc.transactions)
print(acc.borrow(4000))
print(acc.transactions)
print(acc.repayment(7000))
print(acc.transactions)



