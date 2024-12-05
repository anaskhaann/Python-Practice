# Define a function f1 that takes a number num and returns another function
def f1(num):
    def f2(y):
        return y ** num 
    return f2

# Create two instances of f2 with different values of num
a = f1(2)  # a will raise its input to the power of 2
b = f1(3)  # b will raise its input to the power of 3

# Print the memory addresses of the f2 functions
print(a)
print(b)

# Call the f2 functions with y=5
print(a(5))  # Should print 25 (5^2)
print(b(5))  # Should print 125 (5^3)