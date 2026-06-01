class is a collection of data members and function members.
class is a blueprint for creating objects.
self is a reference variable that refers to the current object.
object is an instance of a class.

class pen:
    price=60
    color="blue"
    company="cello"

    def write(self): #self is a reference variable that refers to the current object.
        print(self.price,self.color,self.company)

p1=pen()
p1.price=100
p1.write()            

p2=pen()
p2.color="black"
p2.write()



class student:
    name="raja"
    age=20
    email="sahil0030@gmail.com"

    def display(self):
        print(self.name,self.age,self.email)

s1=student()
s1.display()

s2=student()
s2.name="sahil"
s2.age=22
s2.display()

s3=student()
s3.name="raju"
s3.age=25
s3.display()