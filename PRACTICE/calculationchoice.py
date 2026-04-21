a=int(input("enter a number="))
print(a)
b=int(input("enter b number="))
print(b)

choice=int(input("(enter your choice:")) 



match (choice):
   case 1:
    print("the sum is",a+b)
   case 2:
      print("the sum is",a-b)
   case 3: 
     print("the sum is",a*b)
   case 4:
     print("the sum is",a/b)
   case _:
    print("invalid choice")