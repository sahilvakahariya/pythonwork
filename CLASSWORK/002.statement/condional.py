if else
age=18
if age>18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")


a=100
b=2000
c=360

if a>b:
if a>c:
    print("a is greater ")  
else:
    print("c is greater")


#else:
if b>c:
    print("b is greater")
else:
    print("c is greater")



if a>b and a>c:
   print("a is greater")
elif b>c and b>a:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
else:
    print("something is wrong")

a=int(input("enter a marks="))
print(a)
if a>90 and a<=100:
    print("grade A")
elif a>70 and a<=90:
    print("grade B")
elif a>50 and a<=70:
    print("grade C")
elif a>30 and a<=50:
    print("grade D") 
elif a>=0 and a<=30:
        print("grade E")
else:
    print("invalid marks")




choice=int(input("enter your choice="))
match (choice):
    case 1:print("gujarati")
    case 2:print("english")
    case 3:print("hindi")
    case 4:print("marathi")
