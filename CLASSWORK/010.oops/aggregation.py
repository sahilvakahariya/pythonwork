class salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_salary(self):
        return(self.pay*12)+self.bonus

class employee:
    def __init__(self,name,age,s):
        self.name=name
        self.age=age
        self.salary=s

    def total_salary(self):
        return self.salary.annual_salary()

s=salary(50000,12000)
e=employee("sahil",20,s) 
print(e.total_salary())
