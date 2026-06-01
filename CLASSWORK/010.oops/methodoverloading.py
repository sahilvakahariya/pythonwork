#same name different parameter in same class / opertor over loading use thay che 
from multipledispatch import dispatch   

class wiskey:

    @dispatch(int,int)
    def add(self,a,b):
        print(f"sum of two numbers is {a+b}")

    @dispatch(int,int,int)
    def add(self,a,b,c):
        print(f"sum of three numbers is {a+b+c}")


    #    def add(self*a):
    #     sum=0
    #     for i in a:
    #         sum+=i
    #     print(f"sum of numbers is {sum}")


w=wiskey()
w.add(10,20)        
w.add(10,20,30)        