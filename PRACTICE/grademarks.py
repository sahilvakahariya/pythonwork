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