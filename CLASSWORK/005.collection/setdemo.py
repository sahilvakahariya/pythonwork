s  = {10,20,30,40,50,50}

for i in s:
    print(i)

s.add(100)
print(s)

s.remove(100)
s.discard(50)
s.pop()
print(s)

a={10,20,30,40,50,True,1}
b={30,40,50,60,70,0,False}

print(a.update(b)) 
print(a)

k=a.union(b)
k=a|b
print(a)
print(k)

k=a.intersection(b)        
k=a.intersection_update(b)
k=a&b
print(a)

k=a.difference(b)
k=a.difference_update(b)
k=a-b
print(a)

k=a.symmetric_difference(b)
k=a.symmetric_difference_update(b)
k=a^b
print(a)

