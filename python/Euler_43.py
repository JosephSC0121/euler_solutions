from itertools import permutations
from datetime import datetime

def is_substring_divisible(number):
    primes = [2, 3, 5, 7, 11, 13, 17]
    
    for i, prime in enumerate(primes):
        num = number[i + 1] * 100 + number[i + 2] * 10 + number[i + 3] 
        if num % prime != 0:
            return False
    return True

def pandigital_numbers():
    total = sum(
        int("".join(map(str, number)))
        for number in permutations(range(10))
        if is_substring_divisible(number)
    )
    print(total)

result = pandigital_numbers()

