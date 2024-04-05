# Project Euler Problem #7

import math

def prime_number(n):
    for i in range(2,int(math.sqrt(n)) + 1 ):
        if n % i == 0:
            return False
    return True
def counter():
    i = 1
    counter = 0
    while counter != 10001:
        i += 1
        if prime_number(i) == True:
            counter += 1
    return i
if __name__ == "__main__":
    print(counter())
