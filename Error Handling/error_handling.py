# Two Syntax for File handling

# # Syntax 1
# file = open("youtube.txt","w") #w means write mode it will create file if not present

# # to write something we have to be cautious since maybe it is a imp ifle

# try:
#     file.write("Hello World")
# finally:
#     # Close the file once done
#     file.close()


# Syntax 2

with open("youtube.txt", "w") as file:
    file.write("This is written using syntax 2")
    file.close()