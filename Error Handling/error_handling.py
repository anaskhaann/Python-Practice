# Two Syntax for File handling

file = open("youtube.txt","r") #w means write mode it will create file if not present

# to write something we have to be cautious since maybe it is a imp ifle

try:
    file.write("Hello World")
finally:
    # Close the file once done
    file.close()