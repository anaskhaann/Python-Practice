# username="GlobalVar"

def func():
    # Now this cannot be access outside
    username="LocalVar"
    print(username)
    
func()

# The below print will give error
# print(username)