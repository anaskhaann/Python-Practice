# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = int(input("Enter the Table: "))

for i in range(1,11):
    # Skip the 5th
    if i==5:
        continue
    print(f"{number}x{i}={number*i}")
