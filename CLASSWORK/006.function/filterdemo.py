find odd numbers in list using filter function and lambda function
a=[1,2,3,4,5,6,7,8,9,10]
k=list(filter(lambda x: x % 2 == 1, a))
print(k)

#find even numbers in list using filter function and lambda function
a=[1,2,3,4,5,6,7,8,9,10]
k=list(filter(lambda x: x % 2 == 0, a))
print(k)

find starting with "p" in list using filter function and lambda function
sub=["java","python","php","android","react"]
k=list(filter(lambda x: x.startswith("p"), sub))
print(k)

find containing "a" in list using filter function and lambda function
k=list(filter(lambda element: "a" in element, sub))
print(k)


a=[1,2,3,4,5,6,7,8,9,10]
def checkodd(a):
    if a % 2 == 1:
        return True
k=list(filter(checkodd, a))
print(k)

