# Problem: Keep asking the user for input until they enter a number between 1 and 10.

# Keep asking thus True value in while

while True:
    num=int(input("Enter the number b/w 1 to 10: "))
    
    if (1<= num <=10):
        print("Thanks")
        break
    else:
        print("Error, Enter number between 1 to 10")