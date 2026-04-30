Dictionary is a collection of key-value pairs. It is unordered, mutable, and indexed.
person={    
"name":"sahil",
"age":25,
"city":"pune",
"skills":["python","java","php","android","react"], 
123:"number",
True:"bool",
(10,20,30):"tuple"
}
print(person) 
print(type(person))

Accessing dictionary items:
d=dict(name="sahil",age=25,city="pune")
print(d)

cn={
"india": "In",
"usa": "Us",
"japan": "Jp",
"china": "Ch",
"germany": "Ge"
}
print(cn)
print(cn["india"])  #ye method se dictionary ke value access karte hai key ke through but agar key dictionary me nahi hai to error aata hai
print(cn.get("india1"))  #ye method se dictionary ke value access karte hai key ke through but agar key dictionary me nahi hai to None return karta hai


change dictionary items:
print(cn.keys())   #ye method se dictionary ke sare keys milte hai
print(cn.values()) #ye method se dictionary ke sare values milte hai
print(cn.items())  #ye method se dictionary ke sare key-value pairs milte hai
print(cn)


for i,j in cn.items(): #ye method se dictionary ke sare key-value pairs milte hai aur unhe i,j me store karte hai
    print(i,j)   #ye method se dictionary ke sare keys milte hai 


cn["india"] = "IND"  #ye method se dictionary ke value change karte hai key ke through
cn["france"] = "Fr"  #ye method se dictionary me new key-value pair add karte hai
cn.update({"germany":"GER"})  #ye method se dictionary ke value change karte hai key ke through but ye method se new key-value pair bhi add kar sakte hai
print(cn)


remove dictionary items:
cn.pop("germany")  #ye method se dictionary me se key-value pair remove karte hai key ke through but agar key dictionary me nahi hai to error aata hai
cn.popitem()  #ye method se dictionary me se last key-value pair remove karte hai aur return karta hai
cn.clear()  #ye method se dictionary ke sare key-value pairs remove karte hai but ye method se dictionary delete nahi hota hai
del cn  #ye method se dictionary delete karte hai
print(cn)


#copying a dictionary:
k=cn.copy() #ye method se dictionary ko copy karte hai but ye method se dictionary ko copy karne ke baad bhi original dictionary me changes karne par copied dictionary me bhi changes aate hai
k=cn
k.update({"germany":"G"})
print(cn)
print(k)


nested dictionary:
student={
"name":"sahil",
"age":25,
"email":"sahil@gmail.com",
"skills":["python","java","php","android","react"],
"marks":{"python":90,"java":80,"php":70,"android":60,"react":50}
}

for i,j in student ["marks"].items():
student ["marks"]["python"] = 95
print(student)


x={"name":"sahil","age":25,"city":"pune"}
y=0 #common value for all keys
thisdict = dict.fromkeys(x, y) 
print(thisdict)



x={"name":"sahil","age":25,"city":"pune"}
y={10,20,30}
d=zip(x,y)  #ye method se dictionary ke keys aur values ko zip karte hai but ye method se dictionary banane ke baad bhi original keys aur values me changes karne par zipped dictionary me bhi changes aate hai
print(set(d))

k={"a":10,"b":20,"c":30}
k.setdefault("d",40)  #ye method se dictionary me new key-value pair add karte hai but agar key dictionary me already hai to ye method us key ke value ko change nahi karta hai
print(k)












