# bal = int(input("enter your amount balance: "))
# amount = int(input("Enter the withdrawal amount: "))
# if bal>amount:
#     print(f"= withdrawl accepted")
# elif amount <=0:
#     print("NIL Balance")
# else:
#     print(F"= insufficent balance")

bal = int(input("enter your amount balance: "))
amount = int(input("Enter the withdrawal amount: "))
Rb = bal - amount
if amount % 100 ==0:
    print("withdrawl accepted")
else:
    print(f"= not accepted")
