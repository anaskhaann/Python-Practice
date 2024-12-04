# Problem: Write a function that takes variable number of arguments and returns their sum.

"""Star (*) Indicates that multiple arguments are possible"""

# # Without inbuild
# def sum_all(*args):
#     print(args)
#     print(*args)
#     sum=0
#     for i in args:
#         sum+=i
#     return sum

# With inbuild method

def sum_all(*args):
    return sum(args)

result1=sum_all(1,2,3,4)
result2=sum_all(1,2,3)
result3=sum_all(1,2,3,4,6,7,8)

print(result1)
print(result2)
print(result3)