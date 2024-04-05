import math

def Erastotenes_crib(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(math.sqrt(n) + 1)):
        if is_prime[p]:
            for i in range(p*p, len(is_prime), p):
                is_prime[i] = False
    primes = [x for x in range(len(is_prime)) if is_prime[x]]
    return primes

def find_longest_sum(n):
    primes = Erastotenes_crib(n)
    prime_set = set(primes)
    max_length = 0
    max_sum = 0

    for i in range(len(primes)):
        current_sum = primes[i]
        length = 1

        for j in range(i + 1, len(primes)):
            current_sum += primes[j]
            length += 1

            if current_sum >= n:
                break

            if current_sum in prime_set and length > max_length:
                max_length = length
                max_sum = current_sum

    return max_sum
if __name__ == "__main__":
    print(find_longest_sum(1000000))

