# Write a Python program to import the math module and use functions like sqrt(), ceil(), floor()
import math
num = 25
print("Square root:", math.sqrt(num))
print("Ceil of 4.3:", math.ceil(4.3))
print("Floor of 4.9:", math.floor(4.9))

# Write a Python program to generate random numbers using the random module
import random
print("Random integer:", random.randint(1, 10))
print("Random float:", random.random())
print("Random number (1-100):", random.randint(1, 100))

# Write a Python program to generate random numbers between 1 and 100 using the random module.
import random
for i in range(5):
    print(random.randint(1, 100))
