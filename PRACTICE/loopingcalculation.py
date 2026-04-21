while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("The sum is", a + b)
    elif choice == 2:
        print("The difference is", a - b)
    elif choice == 3:
        print("The product is", a * b)
    elif choice == 4:
        print("The division is", a / b)
    else:
        print("Invalid choice")

    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != 'y':
        break