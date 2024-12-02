# Problem: Compute the factorial of a number using a while loop.

num= int(input("Enter the Number: "))
fact=1
num_temp=num

while num_temp>0:
    fact = fact* num_temp
    num_temp-=1

print(f"The Factorial of {num} is : {fact}")