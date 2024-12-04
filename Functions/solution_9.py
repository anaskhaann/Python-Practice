# Problem: Write a generator function that yields even numbers up to a specified limit.

# Yield means to generate

def even_generator(limit):
    for i in range(2,limit+1,2):
        # print(i)
        # this return will break the function
        # return i
        
        # Yield help to remember the reference as well as loop through it i.e till where we have reach
        # Yield put functions in the memory along with its state
        yield i
        
        
result=even_generator(20)
print(result)

for j in result:
    print(j)