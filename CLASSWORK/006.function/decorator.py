def after(func):
    def execute():
        func()
        print("calling after test")
    return execute

def before(func):
    def execute():
        func()
        print("calling after test")
    return execute

@before
def test():
    print("passing")
test()    


def add(func):
    def execute(*a):
        print("Addtion : ")
        sum = 0
        for i in a:
            sum+=i
        print("addtion is : ",sum)
        func(*a)
    return execute


def mul(func):
    def execute(*a):
        print("Multiplcation : ")
        sum = 1
        for i in a:
            sum*=i
        print("mul is : ",sum)
        func(*a)
    return execute

@add
@mul
def calc(a,b):
    pass
calc(10,20)


def numberonly(func):
    def execute(a):
        if str(a).isalpha():
            func(a)
        else:
            print("invalid num")
    return execute   

@numberonly
def get(a):
    print(a)
get(123)