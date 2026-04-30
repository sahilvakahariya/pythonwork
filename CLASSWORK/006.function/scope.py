local variable
a=10
def test():

    a=50
    print(a)

print(a)
test()
print(a)

#global variable ko function ke andar change karne ke liye global keyword ka use karte hai
a=10
def test():
    global a
    a=50
    print(a)

print(a)
test()
print(a)