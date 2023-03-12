from typing import Type

class Animal:
    def eat(self):
        print('The animal is eating')

    def sleep(self):
        print('The animal is sleeping')

    def walk(self):
        print('The animal is walking')

class Birds(Animal):
    def __init__(self):
        super().__init__()
    
    def sing(self):
        print('The bird is singing')

class Penguin(Birds):
    def __init__(self):
        super().__init__()
    
    def slip(self):
        print('The bird is sliping')

class Person:
    def observe(self, animal: Type[Animal]):
        animal.eat()

robert = Person()
penguin = Animal()
robert.observe(penguin)