# Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

# Divisible by 4 then check if Divisible by 100 and 400 both then also leap year
# Divisible by 100 but not by 400 then not leap year
# help=https://www.scaler.com/topics/images/Java-Leap-Year-Program-577x1024.jpeg


year=int(input("Enter the Year to Check:\n"))

if (year%400==0 or (year%4==0 and year%100!=0)):
    print(f"{year} Year is a Leap year")
else:
    print(f"{year} Year is NOT a Leap year")
    