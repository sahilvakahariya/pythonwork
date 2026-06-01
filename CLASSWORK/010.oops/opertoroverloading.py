#Operator overloading means giving special meaning to operators (+, -, *, ==, etc.) for user-defined objects using magic methods (dunder methods).
class calc:

    def __init__(self,a,b):
        self .a=a
        self .b=b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

    def __mul__(self, other):
        return self.a * other.a, self.b * other.b


c=calc(800,300)
c1=calc(200,100)
print(c+c1)
print(c*c1)