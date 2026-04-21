for j in range(3,100):

    number = j
    flag = 0
    for i in range(2,number):
        if number%i==0:
            flag=1
            break

    if flag==0:
        print(f"{number} is prime number")
    else:
        pass
        print(f"{number } is Not prime")
