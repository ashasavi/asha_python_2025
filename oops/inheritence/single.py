class Animal:
    def eat(self):
       print("Eating.....")

class dog(Animal):
    def bark(self):
        print("Barking...")

a = Animal()  #object for animal
d = dog()      # object for dog

a.eat()
d.bark()
d.eat()