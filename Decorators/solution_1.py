# Problem: Write a decorator that measures the time a function takes to execute.
import time

# Define a decorator function called 'timer' that takes another function 'func' as an argument
def timer(func):
    # Define a new function 'wrapper' that will wrap around the original function 'func'
    def wrapper(*args, **kwargs):
        # Record the start time before calling the original function
        start = time.time()
        
        # Call the original function with its original arguments and return its result
        result = func(*args, **kwargs)
        
        # Record the end time after the original function has finished executing
        end = time.time()
        
        # Calculate and print the execution time of the original function
        print(f"Function {func.__name__} executed in {end - start} seconds")
        
        # Return the result of the original function
        return result
    
    # Return the wrapper function, which will replace the original function when decorated
    return wrapper


# Apply the 'timer' decorator to the 'example' function
@timer
def example(n):
    time.sleep(n)

example(2)
    