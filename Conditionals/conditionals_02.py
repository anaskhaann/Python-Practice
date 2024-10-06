# 2- Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

# age= int(input("Enter Age:"))
# day=(input("Enter the Day of the Week:"))

# if age<18:
#     if day==("wednesday" or "Wednesday"):
#         print("Ticket Price is $6")
#     else:
#         print("Ticket Price is $8")

# elif age>18 and (not("wednesday" or "Wednesday")):
#     print("Ticket Price is $12")
# else:
#     print("Ticket Price is $10 ")


# better SOlution

age=int(input("Enter Age:"))
day=input("Enter Day:")

price=0
if age>18:
    price=12
else:
    price= 8
    
#Alternate for Above Code 
# price = 12 if age>18 else 8

# Check if wednesday then price -2

if day=="Wednesday":
    price = price -2
    # price -=2
else:
    price

print(f"The Price of the Ticket is {price}")