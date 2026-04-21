#  Write a Python program to find a specific string in the list using a simple for loop and if condition. 
List = ['apple', 'banana', 'mango']
search = input("Enter fruit to search: ")

for fruit in List:
    if fruit == search:
        print("Found:", fruit)
        break
else:
    print("Not found")