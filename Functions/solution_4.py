# Problem: Create a function that returns both the area and circumference of a circle given its radius.

def measure_circle(r):
    
    circumference= 2 * 3.14 * r
    area= 3.14* (r**2)
    
    return area, circumference

result= measure_circle(7)
print(result)