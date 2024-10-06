# 2- Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age= int(input("Enter Age:"))
day=(input("Enter the Day of the Week:"))

if age<18:
    if day==("wednesday" or "Wednesday"):
        print("Ticket Price is $6")
    else:
        print("Ticket Price is $8")

elif age>18 and (not("wednesday" or "Wednesday")):
    print("Ticket Price is $12")
else:
    print("Ticket Price is $10 ")