# Problem: Calculate the sum of even numbers up to a given number n.

num= int(input("Enter a number: "))

sumEven=0

for i in range(num+1):
    if i%2==0:
        # print(i)
        sumEven+=i
print(f"The sum of Even numbers upto {num} is {sumEven}")