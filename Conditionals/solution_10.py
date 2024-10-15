#  Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet=input("Cat or Dog?\n").lower()

age=int(input("Enter Age:\n"))

if (pet=="dog" and age<2):
    print("Puppy Food")
elif(pet=="cat" and age>5):
    print("Senior cat food")
else:
    print("Basic Food")
    