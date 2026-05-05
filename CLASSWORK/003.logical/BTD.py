
number = 10011011
p = 0
sum =0
while number!=0:
    rem  = number%10
    sum += (rem*pow(2,p))
    number//=10
    p+=1

print(sum)






# binary base2
# decimal maa 0-9
# octal ma 0-8
# hexadicmal 0-9
# atp toatl hex decimal 0-15