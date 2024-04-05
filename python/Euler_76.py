#Project Euler Problem 76
def primes_sum():
    target = 100
    ns = range(1, target)
    ways = [1] + [0]*target

    for n in ns:
        for i in range(n, target+1):
            ways[i] += ways[i-n]
    return ways[target]


if __name__ == "__main__":
    print(primes_sum()) 
