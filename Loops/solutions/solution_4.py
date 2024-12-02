# Problem: Reverse a string using a loop.

given_str="Sample Text"

rev_str=''

for char in given_str:
    # This will perform shifting of each word to the right side thus making it reverse order
    rev_str = char + rev_str
print(rev_str)