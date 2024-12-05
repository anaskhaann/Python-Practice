x = 99

def calc(y):
    # Here x is global and y is local
    z=x+y
    return z

print(calc(3))