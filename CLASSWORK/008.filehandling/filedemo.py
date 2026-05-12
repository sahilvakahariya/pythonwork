f= open("text.txt","w")
f.write("sahil patel")
f.close()

f= open("text.txt","r")
f.write("sahil patel")
f.writelines(["raju\n","ramesh\n","kenil\n","yash"])
f.close()

f= open("text.txt","a")
f.write("sahil patel")
f.writelines(["raju\n","ramesh\n","kenil\n","yash"])
f.close()

f=open("text.txt","r")
data=f.read()
print(data)
f.close()


f=open("text.txt","r")
while True:
    data=f.readline()
    print(data)
    if not data:
        break

f=open("text.txt","r")
while True:
    data=f.readline()
    if 'e' in data:
        print(data)
    if not data:
        break

f=open("text.txt","r")
while True:
    data=f.readline()
    if data.startswith("k"):
        print(data)
    if not data:
        break

with open("home.txt",'w') as f:
    f.write("sahil patel dindoli")

with open("home.txt",'r') as f:
     print(f.tell())
    f.seek(5)
    data=f.read()
    print(f.tell())
    print(data)

with open("abc.txt",'w+') as f:
    f.write("patel brother")
    f.seek(0)
    data=f.read()
    print(data)


with open("abc.txt",'a+') as f:
    f.write("patel brother")
    f.seek(0)
    data=f.read()
    print(data)


import json
d={"name":"sahil patel","email":"sa@gmail.com"}
with open("data.json",'w') as f:
    json.dump(d,f)


with open("abc.png",'rb') as f:
    data=f.read()
    print(data)