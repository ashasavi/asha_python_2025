# Gdy =int(input("enter the marks gdy:"))
# env =int(input("enter the marks env:"))
# str =int(input("enter the marks str:"))
# bpd =int(input("enter the marks bpd:"))
# hym=int(input("enter the marks hym :"))
# percentage = (((Gdy+env+str+bpd+hym)/500)*100)
# print(f" percentage = {percentage}")
# if percentage>=75:
#     print(f" grade is = A")
# elif percentage >50 and percentage<=75:
#     print(f"grade is = B")
# elif percentage >30 and percentage<=50:
#     print(f"grade is = C")
# else:
#     print(f"grade is = fail")

# a =int(input("enter the marks gdy:"))
# b =int(input("enter the marks env:"))
# c =int(input("enter the marks str:"))
# d =int(input("enter the marks bpd:"))
# e=int(input("enter the marks hym :"))
# percentage = (((a+b+c+d+e)/500)*100)
# print(f" percentage = {percentage}")
# if a or b or c or d or e <30:
#     print(f" = not elegible")
# if percentage>=75:
#     print(f" grade is = A")
# elif percentage >=50:
#     print(f"grade is = B")
# elif percentage >=30:
#     print(f"grade is = C")
# elif percentage < 30:
#     print(f"grade is = fail")

a =int(input("enter the marks gdy:"))
b =int(input("enter the marks env:"))
c =int(input("enter the marks str:"))
d =int(input("enter the marks bpd:"))
e=int(input("enter the marks hym :"))
if 0<= a <=100:
    if 0<= b <=100:
        if 0 <= c <= 100:
            if 0 <= d <= 100:
                if 0 <= e <= 100:
                    percentage = (((a + b + c + d + e) / 500) * 100)
                    print(f" percentage = {percentage}")
if percentage >= 75:
    print(f" grade is = A")
elif percentage >=50:
    print(f"grade is = B")
elif percentage >=30:
    print(f"grade is = C")
elif percentage < 30:
    print(f"grade is = fail")
else:
    print(f" = Fail")

