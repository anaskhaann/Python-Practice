# Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

# My Solution
score=int(input("Enter the Score:"))

if score>=90:
    print("The Student's Grade is A")
elif (score>=80):
    print("The Student's Grade is B")
elif (score>=70):
    print("The Student's Grade is C")
elif (score>=60):
    print("The Student's Grade is D")
else:
    print("The Student's Grade is F")
    