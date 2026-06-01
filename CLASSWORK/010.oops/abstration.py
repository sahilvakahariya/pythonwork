from abc import ABC,abstractmethod

class shape(ABC):

    @abstractmethod
    def area(self):
        pass

class circle(shape):

    @abstractmethod
    def area(self):
        pass


c=circle()
c.area()                