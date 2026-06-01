# Write a Python program to create a class and access its properties using an object. 
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Sahil", 20)
print("Name:", s1.name)
print("Age:", s1.age)

#  Write a Python program to demonstrate the use of local and global variables in a class. 
x = 100  

class Demo:
    def show(self):
        y = 50  
        print("Local Variable:", y)
        print("Global Variable:", x)

obj = Demo()
obj.show()