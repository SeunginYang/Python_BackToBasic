def tax_calculator(income):
    print((income*0.1),"원")

tax_calculator(1000000000)

def add(a,b,c):
    print((a+b+c),"원")

def minus(a,b,c):
    print(((a+b)-c))

def multi(a,b):
    print(a*b)

def div(a,b):
    print(int(a/b))

def square(a,b):
    print(a**b)

def tri(a,b=3):
    print(pow(a,b))

def quadP(welfare):
    print(pow(welfare,4))




add(1000,50,70000)
minus(20,10,15)
multi(15,10)
div(10,2)
square(3,3)
tri(3)
quadP(10)