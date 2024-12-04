# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

"""DOuble star(**) kwargs are used to handle multiple arguments """

def print_kwargs(**kwargs):
    # Since these are multiple named arguments we have to use .item method
    
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    print("")
        
print_kwargs(name="Batman", power="Rich", occupation="Saviour")
print_kwargs(name="SuperMan", power="Laser")
print_kwargs(name="Shaktimaan")