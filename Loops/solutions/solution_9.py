# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

# Unique item i.e sets

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item= set()

for item in items:
    
    # check if it is in the set or not
    if item in unique_item:
        # If yes then duplicate
        print(f"Duplicate Item is '{item}'")
        break
    # add unique to list
    unique_item.add(item)