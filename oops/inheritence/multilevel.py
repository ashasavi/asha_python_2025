class Animal:
    def eat(self):
       print("Eating.....")

class dog(Animal):
    def bark(self):
        print("Barking...")

class puppy(dog):
    def cry(self):
        print("crying...")


a = Animal()  # object for animal
d = dog()  # object for dog
p= puppy()  # object for puppy


a.eat()
d.bark()
d.eat()
p.eat()
p.bark()
p.cry()