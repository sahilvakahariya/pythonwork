# Write a Python program to print a string using a function
def demo():
    print("hello world")
demo()

#Write a Python program to create a function that takes a string as input and prints it
def userinput(text):
    print(text)
userinput("hello python")

#Write a Python program to create a calculator using functions
def calcuation(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
calcuation(20,10)

#Writea Python program to create a parameterized function that takes two arguments and prints their sum.
def sum(a,b):
    print(a+b)
sum(10,20) 

#Write a Python program to create a lambda function with one expression.

squred = lambda a : a*a
print(squred(6))

#Writea Python program to create a lambda function with two expressions.
cal = lambda a , b :(a+b , a*b)
print(cal(10,20))