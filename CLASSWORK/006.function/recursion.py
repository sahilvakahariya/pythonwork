#recursion is a function that calls itself
def square(a):
    print("The square of", a, "is:", a * a)
    a+=1
    if a <= 5:
        square(a)
square(1)