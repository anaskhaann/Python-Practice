"""
This was the question given to me in TCS NQT Test which i failed to solved.
Shame on me

* We have taken input of n = 1 2 3 4 2 4 3
* then we have a list of those number = [1,2,3,4,2,4,3]
* every number is repeated only 2 times and one number is unique we have to  print that number.
"""

n = list(map(int,input().split(" ")))
# print(type(n))

for i in n:
    # print(type(i))
    if n.count(i) == 1:
        print(i)
        