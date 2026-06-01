#multiple inheritance is a one child class inherits from more than one parent class.
class A:
    def test(self):
        print("class a test calling")

class B:
    def sample(self):
      print("class b sample calling")

class c(A,B):
    def demo(self):
        print("class c demo calling")

c=c()
c.test()
c.sample()
c.demo()                     

#multilevel inheritance is a class inherits from another class with itself inherits from a third class

class A:
    def test(self):
        print("class a test calling")

class B(A):
    def sample(self):
      print("class b sample calling")

class c(B):
    def demo(self):
        print("class c demo calling")

c=c()
c.test()
c.sample()
c.demo()

