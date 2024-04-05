# Project Euler Problem #16
import numpy as np
def sum_digits(num):
    return sum(np.array([int(n) for n in str(num)]))  
    
if __name__ == "__main__":
    print(sum_digits(2**1000))

