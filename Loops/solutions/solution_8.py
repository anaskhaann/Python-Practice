# Problem: Check if a number is prime.

num=int(input("Enter the number to check: "))
# Assume that the number is prime
isPrime=True

if num>1:
    for i in range(2,num):
        if (num%i)==0:
            isPrime=False
            break

print(isPrime)
            