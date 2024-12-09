# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.

import time


def cache(func):
    def wrapper(*args):
        pass
    return wrapper



def long_running_function(a,b):
    return a**b
