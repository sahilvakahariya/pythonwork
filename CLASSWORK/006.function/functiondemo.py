# This is a simple function demonstration in Python.
def message():
    print("Hello, World!")
message()  # Calling the function to display the message.

def add(a, b):
    print("The sum is:", a + b)
add(5, 10)  # Calling the function with arguments to display the sum.

def cube(n):
    qu = n*n*n
    return qu  # Calling the function to calculate the cube of 3 and return the result

qu = cube(3)
print("The cube of 3 is:", qu)  # Displaying the result of the cube function.
print(cube(4))  # Calling the cube function directly in the print statement to display the cube of 4.


def square(n):
    sa =n*n
    return sa

sa = square(5)
print("The square of 5 is:", sa)  # Displaying the result of the square function.
print(square(6))  # Calling the square function directly in the print statement to display the square of 6.

def person(name,email="sahil@example.com",age=25):
    print("Name:", name)
    print("Email:", email)
    print("Age:", age)

person("sahil", age=25)  # Calling the person function with arguments to display the person's information.


arbitrary arguments demonstration:
def add(*a):
    sum = 0
    for i in a:
        sum += i
    print("The sum is:", sum)

add(1, 2, 3)  # Calling the add function with multiple arguments to display the sum of the numbers.

#arbitrary keyword arguments demonstration:
def person(**k):
    print(k)
   
person(name="sahil", email="sahil@example.com", age=25) # Calling the person function with keyword arguments to display the person's information.



#lambda function demonstration:
function without name is called lambda function 
add = lambda a, b: a + b  # Defining a lambda function to add two numbers.
print(add(2020,2580))

square = lambda n: n * n  # Defining a lambda function to calculate the square of a number.
print(square(5))  





