num=132
temp =num
sum = 0
while num !=0:
    rem = num%10
    sum+=(pow(rem,3))
    num =num//10

if temp==sum:
    print(f"{temp} is a armstrong")
else:
    print(f"{temp} is not armstrong")