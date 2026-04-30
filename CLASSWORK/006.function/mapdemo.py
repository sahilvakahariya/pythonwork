map function is used to apply a function to all the items in an iterable (list, tuple etc.) and return a map object (an iterator).
a=[1,2,3,4,5,6,7]
k=list(map(lambda x: x*x, a))
print(k)

def square(n):
    return n*n

for i in a:
    j=square(i)
    k.append(j)
print(k)

length of each subject in list:
sub=["java","python","c++","c#"]
k=list(map(lambda x: len(x),sub))
print(list(k))


