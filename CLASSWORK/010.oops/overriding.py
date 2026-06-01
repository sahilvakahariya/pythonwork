#same name same parameter in parent class 
class a:
    def test(self):
        print("i am in class a")

class b(a):
    def test(self):
        print("i am in class b")
        super().test()

b=b()
b.test()                