# Write a Python program to skip 'banana' in a list using the continue statement. List1 = ['apple', 'banana', 'mango'] 
List = ['apple', 'banana', 'mango']
for fruit in List:
    if fruit == 'banana':
        continue
    print(fruit)