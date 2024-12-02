# Problem: Given a string, find the first non-repeated character.
input_str="roller"

for char in input_str:
    print(char)
    # Inbuid count method to check occurance of each characters
    if input_str.count(char)==1:
        print(f"Non Repeated Character is:{char}")