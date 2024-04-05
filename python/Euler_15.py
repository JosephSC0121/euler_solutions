# Euler Project Problem 16

from math import factorial

def factor(n):
    return factorial(n)
def combination(n,k):
    return int(factor(n)/(factor(n-k)*factor(k)))

if __name__ == "__main__":
    print(combination(20*2,20))              
