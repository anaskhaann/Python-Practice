x = 99

# def calc(y):
#     # Here x is global and y is local
#     z=x+y
#     return z

# print(calc(3))


def func2():
    # This will not change the value of x globally
    x= 10
    
func2()
print(x)