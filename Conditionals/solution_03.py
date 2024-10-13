# Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

# Updated Solution
score=int(input("Enter the Score:"))

if score>=101:
    print("Enter the Correct Score Between 0-100")
    exit()
else:        
    if score>=90:
        # print("The Student's Grade is A")
        grade="A"
    elif (score>=80):
        # print("The Student's Grade is B")
        grade="B"
    elif (score>=70):
        # print("The Student's Grade is C")
        grade="C"
    elif (score>=60):
        # print("The Student's Grade is D")
        grade="D"
    else:
        # print("The Student's Grade is F")
        grade="F"

print(f"Grade of the Student is {grade}")

    