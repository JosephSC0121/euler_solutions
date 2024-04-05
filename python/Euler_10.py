# Project Euler Problem #10
import math

def prime_number(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if  n % i == 0:
            return False
    return True

def prime_number_list(num): 
    return sum ([i for i in range(2, num) if prime_number(i) == True])
            
if __name__ == "__main__":
    print(prime_number_list(2000000))

    
