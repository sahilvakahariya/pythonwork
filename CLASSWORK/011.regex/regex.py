# Regular expressions are a powerful tool for matching patterns in strings. They are used for searching, replacing, and manipulating strings based on specific patterns. In Python, the `re` module provides functions for working with regular expressions.
import re #importing the regular expression module
st="my name is sahil and i am 20 years old"

k=re.match("my",st)#check if the pattern match the beginning of the string
print(k)

k=re.search("sahil",st)#search check the whole string
print(k)

k=re.findall("a",st)#findall return the list of all the matches of the pattern in the string
print(k)

k=re.finditer("a",st)#finditer return the iterator of all the matches of the pattern in the string
print(next(k))
print(next(k))

k=re.sub("sahil","sahil khan",st)#replace the pattern with the new string and return the new string
print(k)

k=re.split("sahil",st)#split the string by occurrence of the pattern
print(k)


number=input("enter a number:")
k=re.match(r"^[0-9]{10}$",number)
if k is None:
    print("invalid number")
else:
    print("valid number")


string=input("enter a character:")
k=re.match(r"^[a-z]{1,10}$",string)
if k is None:
    print("invalid character")
else:
    print("valid character")



email="sahil@gmail.com"
k=re.match("^[a-z0-9_-]+@[a-z]+\\.[a-z]{2,4}$",email)
print(k)



password=input("enter a password:")
k=re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",password)
if k is None:
    print("invalid password")
else:
    print("valid password")






