#Write a Python program to create a dictionary from two lists, one containing keys and the other containing values. Then print the resulting dictionary.

keys = ["name","age","city"]
values =["sahil",20,"surat"]

d= {}
for i in range(len(keys)):
    d[keys[i]]= values[i]
print(d)
