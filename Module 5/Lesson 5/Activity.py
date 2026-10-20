from abc import ABC, abstractmethod

class AbsClass(ABC):

    def print(self, x):
        print("Value:", x)

    @abstractmethod
    def task(self):
        print("Wr are an abstract method")


class test_class(AbsClass):

    def task(self):
        print("We are working to show the abstract class.")

obj = test_class()
obj.task()
obj.print(100)