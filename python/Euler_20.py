# Project Euler Problem #20
import numpy as np
def factorial(n):
    result = 1
    for i in range (1,n+1):
        result *= i
    return result

def sum_digits(num):
    return sum(np.array([int(n) for n in str(factorial(num))]))  
    
if __name__ == "__main__":
    print(sum_digits(100))
