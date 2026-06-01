class salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_salary(self):
        return(self.pay*12)+self.bonus

class employee:
    def __init__(self,name,age,pay,bonus):
        self.name=name
        self.age=age
        self.salary=salary(pay,bonus)

    def total_salary(self):
        return self.salary.annual_salary()

e=employee("sahil",20,50000,12000) 
print(e.total_salary())
