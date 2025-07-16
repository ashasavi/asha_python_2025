class student:
    def __init__(self,name,usn):
        self.name = name
        self.usn = usn
    def printdetails(self):
        print(f"name is {self.name},USN is{self.usn}")

s1 = student("asha", 123)
s2 = student("abhishek",234)

s1.printdetails()
s2.printdetails()




