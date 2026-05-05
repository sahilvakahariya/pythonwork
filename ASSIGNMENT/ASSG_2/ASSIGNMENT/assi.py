simple calculator using functions

def calculator():
    print("===============calculator===============")

    a = int(input("Enter  number 1: "))
    b = int(input("Enter  number 2: "))

    choice = "y"
    while choice != "n":
        ch = input("enter your choice = ")
        match ch:
            case "1": print("addition is =", a + b)
            case "2": print("subtraction is =", a - b)
            case "3": print("multiplication is =", a * b)
            case "4": print("division is =", a / b)
        choice = input("do you want to continue (y/n) = ")
        if choice == "n":
            print("a maru cal che hu use karis")
        
calculator()


grade mangement system

def grade_system():
    print("===============grade management system===============")

    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))

    if marks >= 90:
        grade = "A destination"
    elif marks >= 80:
        grade = "B first class"
    elif marks >= 70:
        grade = "C second class"
    elif marks >= 60:
        grade = "D third class"
    else:
        grade = "F fail"

    print(f"Student Name: {name}")
    print(f"Marks: {marks}") 
    print(f"Grade: {grade}") 

grade_system()