class Animal:
    def eat(self):
       print("Eating.....")

class dog(Animal):
    def bark(self):
        print("Barking...")

class cat(Animal):
    def meow(self):
        print("meowing...")

a = Animal()  #object for animal
d = dog()      # object for dog
c = cat()

a.eat()
d.bark()
d.eat()
c.meow()
c.eat()