# a = input("enter the name:")
# m1 = int (input("enter the marks:"))
# if m1 >= 0 and m1 < 100:
#     print(f" {m1}")
# else:
#     print(f" invalid")

a = input("enter the name:")
m1 = float(input("enter the marks:"))
if m1 >= 0 and m1 <= 40:
       print(f"m1 = grade E")
elif m1>40 and m1<=60:
    print(f" m1 =grade D")
else:
    print(f" invalid")


