username="GlobalVar"

def func():
    # Now this cannot be access outside
    username="LocalVar"
    print(username)
    
func()

# This will print global
print(username)