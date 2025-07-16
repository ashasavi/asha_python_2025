from abc import ABC, abstractmethod

class Animal(ABC):

    @ abstractmethod
    def eat(self):
        pass
class dog(Animal):
    def eat(self):
        print("dog food")

d = dog()
d.eat()