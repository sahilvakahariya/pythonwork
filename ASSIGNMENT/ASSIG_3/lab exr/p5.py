# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input). 
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")

finally:
    print("Program Ended.")

# Write a Python program to demonstrate handling multiple exceptions. 
try:
    num = int(input("Enter a number: "))
    result = 10 / num

    mylist = [1, 2, 3]
    print(mylist[5])

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except IndexError:
    print("List index out of range.")

finally:
    print("Program Ended.")

# Write a Python program to handle file exceptions and use the finally block for closing the file.
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Unable to read file.")
finally:
    if 'file' in locals():
        file.close()
    print("File handling completed.")

# Write a Python program to print custom exceptions. 
class CustomException(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise CustomException("This is a custom exception.")
except CustomException as e:
    print("Caught custom exception:", e.message)
