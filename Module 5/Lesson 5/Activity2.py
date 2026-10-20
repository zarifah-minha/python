from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk")

class Dog(Animal):
    def move(self):
        print("I can bark")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Lion(Animal):
    def move(self):
        print("I can roar")

h = Human()
h.move()

d = Dog()
d.move()

s = Snake()
s.move()

l = Lion()
l.move()