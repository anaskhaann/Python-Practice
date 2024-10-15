# Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

# Divisible by 4 then check if Divisible by 100 and 400 both then also leap year
# Divisible by 100 but not by 400 then not leap year
# help=https://www.scaler.com/topics/images/Java-Leap-Year-Program-577x1024.jpeg


year=int(input("Enter the Year to Check:\n"))


if (year%4==0):
    if (year%100==0):
        if (year%400==0):
            print(f"The year {year} is a Leap Year")
        else:
            print(f"The year {year} is NOT a Leap Year")    
    else:
        print(f"The year {year} is a Leap Year")
else:
    print(f"The year {year} is NOT a Leap Year")    
