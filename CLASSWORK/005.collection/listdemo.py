l=list((10,20,30,40,50,"sahil",25.2))
print(l)
print(type(l))
print(len(l))
print(l[0])

# access list item :  
l = [10,20,30,40,50,60]   
print(l[1])
print(l[1:5])      #ye index se list ke element access karte hai starting index se end index tak but end index ke element ko include nahi karte hai
print(l[::2])        #ye operator se list ke element ko step ke according access
print(l[-1])        #ye negative index se list ke element access karte hai starting index se end index tak but end index ke element ko include nahi karte hai   
print(l[-4:-1])      #ye negative index se list ke element access karte hai starting index se end index tak but end index ke element ko include nahi karte hai
print(l[::2])        #ye operator se list ke element ko step ke according access karte hai but step ke according element ko include karte hai
print(l[::-1])      #ye operator se list ke element ko reverse order me access karte hai

change list

l = [10,20,30,40,50,60]

l[0] = 100
l.insert(3,300)
l.append(300)
l[:5] = [45,46,78,98,98,74,85,41]
print(l)

a  = [10,20,30]
b = [40,50,60]

a.extend(b)
print(a)



remove

l = [10,20,30,40,50,60]
# l.remove(2)
l.pop(2)

l.clear()
del l
print(l)


for i in l:
    print(i)

for i in range(len(l)):
    print(l[i])

i=0
while i<len(l):
    print(l[i])
    i+=1




s = ["python","java","php","android","react"]
l = []
for i in s:
    if "a" in i:
        l.append(i)
print(l)

l = [i for i in s if "a" in i]
print(l)

k = [i for i in s if i.startswith('p')]
print(k)



s = ["python","java","php","android","react"]
s.sort()                 #ye method se list ko sort karte hai
s.sort(reverse=True)   #ye method se list ko reverse order me sort karte hai
s.reverse()           #ye method se list ko reverse karte hai

k = sorted(s)
print(k)

k = s
k = s.copy()        #ye method se list ko copy karte hai but ye list ko copy karne ke baad bhi original list me changes karne par copied list me bhi changes aate hai
k = list(s)
k = s[:]

k.append(5000)      #ye method se list me element add karte hai but ye method se list me element add karne ke baad bhi original list me changes karne par copied list me bhi changes aate hai
print(k)
print(s)