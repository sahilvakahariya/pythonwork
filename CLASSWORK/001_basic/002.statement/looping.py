for i in range(10):
    print(i)

for i in range(5,10):
    print(i)

for i in range(1,10,3):
    print(i)

for i in range(10,0,-2):
    print(i)

i=21
while i<20:
    print(i)
    i+=1


choice="y"

while choice !="n":
    a=int(input("enter a marks="))
if  a>90 and a<=100:
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

    choice=input("do you want to continue? press y or n")