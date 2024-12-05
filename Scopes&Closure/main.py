x=10

def f1():
    x=20
    def f2():
        print(x)
    return f2

result= f1()
print(result)
result()