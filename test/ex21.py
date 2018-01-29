def add(a,b):
    print("adding %d+%d"%(a,b))
    return a+b

def subtract(a,b):
    print("subtracting %d-%d"%(a,b))
    return a-b

def multiply(a,b):
    print("multiplying %d*%d"%(a,b))
    return a*b

def divide(a,b):
    print("diving %d/%d"%(a,b))
    return a/b

age = add (30,5)
height =subtract(78,4)
weight =multiply(90,2)
iq =divide(100,2)

print("Age:%d,Height:%d,Weight:%d,Iq:%d"%(age,height,weight,iq))