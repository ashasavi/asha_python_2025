name = input("Enter your name: ")
age = int(input("Enter your age:"))
empid = int(input("Enter your empid: "))
#This line below is without formated string
print("your name is "   + name + " and your age is "  + str (age) + "and your empid is: ", empid)
#This is an example of formatted strings
print(f" your name is {name} and your age is {age} and your empid is {empid}")