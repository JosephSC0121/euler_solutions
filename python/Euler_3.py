# Project Euler Problem #3
import math 

def largest_prime_factor(n):
    factors = []
    for i in range(2,int(math.sqrt(n))+1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)

    return max(factors)

if __name__ == "__main__":
    print(largest_prime_factor(600851475143))

