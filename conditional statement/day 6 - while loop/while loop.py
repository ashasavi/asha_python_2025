# i = 10
# while i<15:
#     print(i)
#     i+=1

# i = 10
# while i<15:
#     print("hello BMS", end =' ')
#     i+=1

# i = 1
# while i<101:
#     print(i)
#     i+=1


# n = int(input("enter a num:"))
# is_prime = True
# if n<2:
#     is_prime= False
# else:
#     i=2
#     while i<n:
#         if n%i==0:
#             is_prime = False
#             break
#         i+=1
# print("prime" if is_prime else "not prime")


# n = int(input("entr a num between 1 to 3: "))
# if n==1:
#         print(f" hello= 1")
# elif n==2:
#         print (f" bye = 2")
# else:
#         print(f" exit = 3")
# while n>=3:
#         print(f"program complete")
#         break

while True:
    print("1. say hello\n2.say bye\n3.exit")
    choice = int(input("enter a choice:"))
    if choice ==1:
        print(f"say hello")
    elif choice ==2:
        print(f"say bye")
    elif choice ==3:
        print("ok exiting . .")
        break
    else:
        print("invalid choice!")
