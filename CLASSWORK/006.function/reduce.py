#reduce use in single iterable and return single value
from functools import reduce
# l=[10,20,30,40,50,60,70,80,90,100]
# r=reduce(lambda a,b: a if a>b else b,l)
# print(r)
# r=reduce(lambda a,b: a if a<b else b,l)
# print(r)  
# r=reduce(lambda a,b: a+b,l)
# print(r)
# l=[1,2,3,4,5]
# def sum(a,b):
#     return a+b  
# k=0
# for i in l:
#     k=sum(k,i)
# print(k)