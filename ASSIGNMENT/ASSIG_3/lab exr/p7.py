# Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.). 
# Single Inheritance
class Parent:
    def show(self):
        print("Parent Class")

class Child(Parent):
    pass

c= Child()
c.show()

# Multiple Inheritance
class Father:
    def father(self):
        print("Father's method")
class Mother:
    def mother(self):
        print("Mother's method")
class Child(Father, Mother):
    pass

c = Child()
c.father()
c.mother()

# Multilevel Inheritance
class Grandparent:
    def grandparent(self):
        print("Grandparent's method")
class Parent(Grandparent):
    def parent(self):
        print("Parent's method")
class Child(Parent):
    def child(self):
        print("Child's method")
c = Child()
c.grandparent()
c.parent()
c.child()

# hybrid Inheritance
class A:
    def method_a(self):
        print("Method A")
class B(A):
    def method_b(self):
        print("Method B")
class C(A):
    def method_c(self):
        print("Method C")
class D(B, C):
    def method_d(self):
        print("Method D")
d = D()
d.method_a()
d.method_b()
d.method_c()
d.method_d()       

# hierarchy of inheritance
class Parent:
    def parent(self):
        print("Parent's method")
class Child1(Parent):
    def child1(self):
        print("Child1's method")
class Child2(Parent):
    def child2(self):
        print("Child2's method")    

c1 = Child1()
c2 = Child2()
c1.parent()
c1.child1()
c2.parent()
c2.child2()

# Write a Python program to demonstrate the use of the super() function in inheritance.
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

d = Child("Sahil", 20)
d.display()
