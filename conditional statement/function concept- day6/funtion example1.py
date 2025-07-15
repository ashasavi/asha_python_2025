# def greet():
#     print("good morning")
#     print("have a nice day")
#
# greet()

# def add(x,y):
#     total = a+b
#     return total
# sum = add(10,20)
# print(sum)

# def add(x,y):
#     total = x+y
#     return total
# print(add(10,20))

# def add(x,y):
#     total = x+y
#     return total
# num1 =int(input("enter num1:"))
# num2 = int(input("enter num2: "))
#
# print(add(num1,num2))

# MATCH CASE
# print("1.add\n 2.subtract\n 3.multiply")
# choice = int(input("enter the choice: "))
# def add(a,b):
#     total = a+b
#     return total
# def subtract(a,b):
#         total = a-b
#         return total
# def multiply(a,b):
#             total = a*b
#             return total
#
# num1 = int(input("enter the num1:"))
# num2= int(input("enter the num2: "))
# match choice:
#     case 1:
#         print(add(num1,num2))
#     case 2:
#         print(subtract(num1,num2))
#     case 3:
#         print(multiply(num1,num2))
#     case _:
#         print("invalid entry")



# ifelse
# print("1.add\n 2.subtract\n 3.multiply")
# choice = int(input("enter the choice: "))
# def add(a,b):
#     total = a+b
#     return total
# def subtract(a,b):
#         total = a-b
#         return total
# def multiply(a,b):
#             total = a*b
#             return total
#
# num1 = int(input("enter the num1:"))
# num2= int(input("enter the num2: "))
# if choice == 1:
#     print(f"sum=",add(num1,num2))
# elif choice == 2:
#     print(f" subtract =",subtract(num1,num2))
# elif choice ==3:
#     print(f"multiply = ", multiply(num1,num2))
# else:
#     print(f"invalid entry")


print("1.add\n 2.subtract\n 3.multiply\n 4.div")
choice = int(input("enter the choice: "))
def add(a,b):
    total = a+b
    return total
def subtract(a,b):
        total = a-b
        return total
def multiply(a,b):
            total = a*b
            return total
def div(a, b):
    total = a / b
    return total

while True:
    num1 = int(input("enter the num1:"))
    num2= int(input("enter the num2: "))
    if choice == 1:
        print(f"sum=",add(num1,num2))
    elif choice == 2:
        print(f" subtract =",subtract(num1,num2))
    elif choice ==3:
        print(f"multiply = ", multiply(num1,num2))
    elif choice ==4:
        print(f"div = ", div(num1,num2))
    else:
       print(f"invalid entry")
    break


r