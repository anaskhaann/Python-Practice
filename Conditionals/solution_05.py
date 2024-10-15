# Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

# Converting input of user to our format for comparision
weather=input("enter the weather today: ").lower()

if weather== "sunny":
    print("Go for walk")
elif weather== "rainy":
    print("Read a book")
elif weather== "snowy":
    print("Build a Snowman")
else:
    print("Do whatever you like")