def test()
try:
    a=int(input("enter a num:"))
    return a
except Exception as e:
    return e
finally:
    print("hello program ended")

print(test())    
