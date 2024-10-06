# 1- Classify a Person's Age Group: Child(<13), Teen(13-19), Adult(20-49),Senior(50+)


age= int(input("Enter the Age:"))

if age <13:
    print("Child")
elif age<20:
    print("Teenager")
elif age<50:
    print("Adult") 
else:
    print("Senior")   


