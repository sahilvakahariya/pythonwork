from abc import ABC,abstractmethod

class account(ABC):
    balance=0
    def check_balance(self):
        print(f"current balance is ,{self.balance}")

    @abstractmethod
    def depositer(self,amount):
        pass        #pass means empty body of function
 
    @abstractmethod
    def withdraw(self,amount):
        pass


class saving(account):
    def depositer(self,amount):
      self.balance+=amount

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount

class loan(account):
    def depositer(self,amount):
        if amount>self.balance:
            k=amount-self.balance
            print(f"loan cleared,you have left {k} amount to pay")
            self.balance=0
        else:
            self.balance-=amount

        def withdraw(self,amount):
            self.balance+=amount
      
        

# s=saving()
# s.depositer(1000)
# s.check_balance()
# s.withdraw(5000)
# s.check_balance()     


l = loan()
l.check_balance()
l.withdraw(5000)
l.check_balance()
l.depositer(2000)
l.check_balance()