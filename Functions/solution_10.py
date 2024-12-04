# Problem: Create a recursive function to calculate the factorial of a number.

# In recursion first check the exit condition

def fact(n):
    # Check exit condition
    if n==0:
        return 1
    else:
        return n* fact(n-1)

print(fact(20))