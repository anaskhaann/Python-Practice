# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    
    def wrapper(*args,**kwargs):
    
        args_value=", ".join(str(arg) for arg in args)
        kwrgs_value=", ".join(f"{k}:{v}" for k,v in kwargs.items())
    
        print( f" Calling the Function: {func.__name__},With Arguments: {args_value} And KeyWord Arguments: {kwrgs_value} " )
    
        return func(*args,**kwargs)
    
    return wrapper

@debug
def example(name,greetings="Hello Guys!!"):
    return f"{greetings}, {name}"
    
example("anas","Good Morning")