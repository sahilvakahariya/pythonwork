t = (10,20,30,40,50,"ddsd",56.44)
t = tuple((10,20,30))
print(t)
print(type(t))
print(len(t))


t = ("python","java","php","android")

k = list(t)
k.append("React")
t = tuple(k)
print(t)


(*a,b) = ("python","java","php","android")

print(a)  
print(b)

print(t*2) #ye operator se tuple ke sare element 2 times print hote hai

del t
print(t)

k = [10]
print(type(k))
l = (10,)
print(type(l))