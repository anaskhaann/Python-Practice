"""
Problem : Sum of Digits
Write a Python function that takes a positive integer as input and returns the sum of its digits.

Example Input/Output
Input: 12345
Output: 15 (1 + 2 + 3 + 4 + 5)

Input: 9876
Output: 30 (9 + 8 + 7 + 6)

Constraints:
* The input will always be a positive integer.
* You cannot use built-in functions like sum(map(int, str(num))).
"""


num = (input("Enter a number: "))

sum=0

for i in num:
    sum+= int(i)

print(sum)