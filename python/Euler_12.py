# Project Euler Problem #12
import math
import time

def triangle_number(x):

    n = (-1 + math.sqrt(1 + 8 * x)) / 2

    if n == int(n) and n > 0:
        return True
    return False

def triangle_divisors():
    div = 0
    i = 0
    while div < 500:
        i += 1
        div = -1
        if triangle_number(i) == True:
            for x in range(1, int(math.sqrt(i))+1):
                if i % x == 0:
                    div += 2
    return i 

if __name__ == "__main__":
    start = time.time()
    print(triangle_divisors())            
    end = time.time()
    print(end - start)
