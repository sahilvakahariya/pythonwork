#inheritance is a parent child relationship between two classes.
class A:
    id= 10

    def test(self):
        print("class a test calling")

class B(A):
    id=20
    def sample(self):
      print(self.id) #child class can access parent class data.
      print(super().id) #super() is used to access parent class data.
      print(A.id)


b=B()
b.sample()      
b.test() #child class can access parent class function.


