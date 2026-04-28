s  = {10,20,30,40,50,50}

for i in s:
    print(i)

s.add(100)
print(s)

s.remove(100)   #ye method se set me se element remove karte hai but agar element set me nahi hai to error aata hai
s.discard(50)   #ye method se set me se element remove karte hai but agar element set me nahi hai to error nahi aata hai``
s.pop()        #ye method se set me se random element remove karte hai aur return karta hai
print(s)

a = {10, 20, 30, 40, 50}
b = {30, 40, 50, 60, 70}
print(a.update(b)) #ye method se a set me b set ke sare element add ho jate hai but ye a set ko update kar deta hai
print(a)

print(a.union(b)) #ye method se dono set ke sare element milte hai without duplicate
k=a|b   #ye operator se dono set ke sare element milte hai without duplicate
print(k)

k=a.intersection(b)   #method se common element milte hai dono set me
k=a.intersection_update(b)  #ye method se common element milte hai dono set me but ye a set ko update kar deta hai
k=a&b   #ye operator se common element milte hai dono set me
print(k)

k=a.symmetric_difference(b)  #ye method se dono set me jo common element nahi hai wo milte hai
k=a.symmetric_difference_update(b)  #ye method se dono set me jo common element nahi hai wo milte hai but ye a set ko update kar deta hai
k=a^b   #ye operator se dono set me jo common element nahi hai wo milte hai
print(k)

k=a.difference(b)  #ye method se a set me jo element hai but b set me nahi hai wo milte hai
k=a.difference_update(b)  #ye method se a set me jo element hai but b set me nahi hai wo milte hai but ye a set ko update kar deta hai
k=a-b   #ye operator se a set me jo element hai but b set me nahi hai wo milte hai
print(k)


