def sum_of_squares(n):
    return sum(int(digit) ** 2 for digit in str(n))

def chain_ends_at_89(n, cache={}):
    if n in cache:
        return cache[n]
    
    sequence = []
    while n != 1 and n != 89:
        sequence.append(n)
        n = sum_of_squares(n)
    
    result = (n == 89)
    for num in sequence:
        cache[num] = result
    
    return result

count = sum(1 for i in range(1, 10_000_000) if chain_ends_at_89(i))

print(count)
