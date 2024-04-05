# Project Euler Problem #3
import math

def is_fibonacci(n):
    # Check if the number is a perfect square
    root1 = math.isqrt(5*n*n + 4)
    root2 = math.isqrt(5*n*n - 4)
    if root1**2 == 5*n*n + 4 or root2**2 == 5*n*n - 4:
        return True
    else:
        return False

def comparation():
    add = 0
    for i in range(1,10):
        if is_fibonacci(i)==True and i%2==0:
            add += i
    return add

if __name__ == "__main__":
    print(comparation())

