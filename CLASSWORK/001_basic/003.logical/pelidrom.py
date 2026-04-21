number = 1234554321
temp = number
sum = 0
while number!=0:
    rem = number%10
    sum = (sum*10) + rem
    number=number//10

if temp==sum:
    print("pelidrom")
else:
    print("not pelidrom")