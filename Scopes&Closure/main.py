x = 99

# def calc(y):
#     # Here x is global and y is local
#     z=x+y
#     return z

# print(calc(3))


def func2():
    # This will not change the value of x globally
    
    # To change this use keyword "global" but this is not a good practice
    global x
    x=10
    
    
func2()
print(x)