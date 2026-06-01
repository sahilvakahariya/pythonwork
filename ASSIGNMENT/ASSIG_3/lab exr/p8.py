# Write Python programs to demonstrate method overloading and method overriding
# Method Overloading
class Demo:
    def add(self, a, b=0):
        print("Sum =", a + b)

d= Demo()
d.add(10)
d.add(10, 20)

# Method Overriding
class Parent:
    def show(self):
        print("Parent Class")
        
class Child(Parent):
    def show(self):
        print("Child Class")

p = Parent()
c = Child()
p.show()
c.show()