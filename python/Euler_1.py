# Project Euler Problem #1
import time

def sumDiv(n):
    return sum([i for i in range(1, n)if i%5 == 0 or i%3 == 0])

if __name__ == "__main__":
    print(sumDiv(1000))
