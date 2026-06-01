class pen:

    def __init__(self,name,price,colour,company):
        self.name=name
        self.price=price
        self.colour=colour
        self.company=company

    def display(self):
        print(self.name,self.price,self.colour,self.company)
        
class notebook(pen):
    def __init__(self,name,price,colour,company,pages):
        super().__init__(name,price,colour,company)
        self.pages=pages

    def display(self):
        super().display()
        print(self.pages)        

p=pen("reynolds",10,"blue","reynolds")
p.display()        

n=notebook("reynolds",10,"blue","reynolds",100)
n.display()