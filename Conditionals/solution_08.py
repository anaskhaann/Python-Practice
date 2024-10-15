#  Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password=input("Enter the Password:\n")

if len(password)<6:
    print("Weak Password")
elif len(password) <=10:
    print("Medium Password")
else:
    print("Strong Password")
