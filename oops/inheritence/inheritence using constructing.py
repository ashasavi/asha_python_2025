# class parent:
#     def __init__(self):
#         print("this is parent constructor")
#
# class child(parent):
#     def __init__(self):
#        print("this is child constructor")
#
# c = child()



# class parent:
#     def __init__(self):
#         print("this is parent constructor")
#
# class child(parent):
#     def __init__(self):
#         super().__init__()  #calls the paernt constructor
#         print("this is child constructor")
#
# c = child()

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class student(person):
    def __init__(self,name,age ,usn):
        super(). __init__(name, age)
        self.usn = usn

    def printdetails(self):
        print(f"name is {self.name},age is {self.age}, USN is{self.usn}")

s = student("asha",47,123)
s.printdetails()


