# Project Euler Problem #45
import math
def is_pentagonal(p):
    if (math.sqrt(24*p+1)+1)%6 == 0:
        return True
    return False


def is_hexagonal(h):
    
    if (math.sqrt(8*h+1)+1) %4 == 0:
        return True
    return False

# iterator start after 285
i = 286

# while loop for iterating
while True:
    triangle = i*(i+1)/2
    if is_pentagonal(triangle) and is_hexagonal(triangle):
        print (triangle)
        break
    i += 1

