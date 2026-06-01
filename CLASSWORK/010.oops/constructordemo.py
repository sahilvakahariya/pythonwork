class student:

    def __init__(self,name,age,email): #constructor is a special method called automatically when we create an object of the class
        self.name=name
        self.age=age
        self.email=email

    def display(self):
        print(self.name,self.age,self.email)

s=student("sahil",22,"sahil0030@gmail.com")
s.display()

s1=student("raja",20,"raja@gmail.com")
s1.display()



class product:

    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def display(self):
        print(self.name,self.price,self.quantity)

p=product("laptop",500000,10)
p.display()


class Student:

    clg = "XYZ"
    def __init__(self,name,email,age):
        self.name = name
        self.email =email
        self.age = age

    def display(self):
        print(self.name,self.email,self.age,self.clg)

    @classmethod
    def test(cls):
        print(cls.clg) #class method can access only class data.

    @staticmethod
    def demo(): #static method is a work in normal function .
        print("static calling")
        


Student.clg="ABC"

s = Student("sahil","sahil@gmail.com",24)
s.display()

s1 = Student("Kenil","kenil@gmail.com",22)
s1.display()

Student.test()
Student.demo()


