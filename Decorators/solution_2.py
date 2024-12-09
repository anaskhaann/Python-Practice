# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        # Format the positional arguments into a string
        args_value = ", ".join(str(arg) for arg in args)
        
        # Format the keyword arguments into a string
        kwrgs_value = ", ".join(f"{k}:{v}" for k, v in kwargs.items())
        
        # Print a message indicating the function name and its arguments
        print(f"Calling the Function: {func.__name__}, With Arguments: {args_value} And Keyword Arguments: {kwrgs_value}")
        
        # Call the original function 'func' with the original arguments and return its result
        return func(*args, **kwargs)
    
    return wrapper

@debug
def example(name,greetings="Hello Guys!!"):
    return f"{greetings}, {name}"
    
example("anas","Good Morning")