# Problem: Write a decorator that measures the time a function takes to execute.
import time

# This is template structure for decorators, function inside function
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result = func(*args,**kwargs)
        end= time.time()
        print(f" function {func.__name__} execute in {end-start} seconds")
        return result
    return wrapper

def example(n):
    time.sleep(n)

example(2)
    