# number = 155
# st = ""
# while number !=0:
#     rem = number%2
#     st = str(rem) + st
#     number//=2  
# print(st)



number = 468
st = 0
mul=1
while number !=0:
    rem = number%2
    st = (rem*mul) + st
    number//=2  
    mul*=10
#10100
print(st)