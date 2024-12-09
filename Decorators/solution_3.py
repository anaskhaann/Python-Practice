# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.

import time


def cache(func):
    # Create a dictionary to store cached values for easy access
    cache_value = {}
    
    def wrapper(*args):
        # Check if the function arguments are already in the cache
        # This is done by checking if the 'args' tuple is a key in the 'cache_value' dictionary
        if args in cache_value:
            # If cached, return the cached value
            # This avoids the need to recompute the result, making the function call faster
            return cache_value[args]
        
        # If not cached, call the original function 'func' with the arguments
        # This will compute the result for the given arguments
        result = func(*args)
        
        # Store the result in the cache for future use
        cache_value[args] = result
        
        # Return the result
        return result
    
    return wrapper


@cache
def long_running_function(a,b):
    time.sleep(4)
    return a**b

# First execution will take time
print(long_running_function(2,3))
# second execution wont run the function but will fetch the result from cache since both are same
print(long_running_function(2,3))


print(long_running_function(5,3))
print(long_running_function(5,3))
