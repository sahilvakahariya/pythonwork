#arithmetic opertors(+,-,*,/,%,//)

a=10
b=20

print(a+b)
print("hello"+"sahil")
print(str(a)+"patel")
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b) 
print(a**b)



#assignment opertors(+=,-=,*=,/=,**=,//=,)
a=10

a+=20
a-=5
a*=80  
a/=2    
a//=5 
a**=20   
print(a)


#logical opertors(and,or,not)

print("true"and "true")
print("true"and "false")
print("false"and "true")
print("false"and "false")


print("true"or "true")
print("true"or"false")
print("false"or "true")
print("false"or "false")

print (not true)

username="admin"
password="admin"
print(password=="admin" and username=="admin")
print(password=="admin" or username=="admin")

#comparison or relational(==,<,>,<=,>=,!=)

a=20
b=60
c=20

print(a==b)
print(a>=b)
print(a<=c)
print(a==c)
print(a!=b)


#identity : is isnot
a=10
b=10

a=[10,20]
b=[10,20]
c=a
a.append(50)
print(a)
print(b)
print(a is not b)
print(a is c)

#membership in,not in
a=[10,20,30]
print(100 not in a)

a=(10,20)
b=(10,20)
print(a is b)
