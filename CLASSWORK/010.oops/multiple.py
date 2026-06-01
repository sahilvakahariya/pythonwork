class a:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("class a constructor calling")

        def display(self):
            print(self.name,self.age)

class b:
    def __init__(self,name):
        self.name=name
        self.age=age
        print("class b constructor calling")

        def display(self):
            print(self.name,self.age)

class c(a,b):
    def __init__(self,name,age):
        b(name,age).__init__(name,age)


c=c("sahil",20)
c.display()

                                