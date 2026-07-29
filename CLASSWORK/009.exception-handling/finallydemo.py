def test():
try:
    a=int(input("enter a num:"))
    return a
except Exception as e:
    return e
finally:
    print("hello program ended")

print(test())    

#try block is used to handle exceptions.
#except block is used to handle exceptions.
#finally block is used to execute code regardless of whether an exception occurred or not.