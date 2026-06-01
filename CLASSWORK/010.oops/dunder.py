class demo:

    name="sahil"
    def __str__(self):
        return self.name

d=demo()
print(d)


class calc:

    def  __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def __eq__(self,value):
        return self.num1==value.num1 and self.num2==value.num2

c=calc(10,20)
c1=calc(10,200)
print(c==c1)


class sample:

    def __init__(self,a):
        self.a=a

    def __len__(self):
        return len(self.a)

    def __setitem__(self,key,value):
        self.a[key]=value

    def __getitem__(self,key):
        return self.a[key]

s=sample([1,2,3])
print(len(s))
s[0]=100
print(s.a)
