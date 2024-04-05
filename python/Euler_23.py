# Euler Project Problem 23
from math import sqrt

def non_abundant():
    non_abund = []
    for i in range(1, 28124):
        div_sum = 0
        for x in range(1, int(sqrt(i)) + 1):
            if i % x == 0:
                div_sum += x
                if x != i // x:
                    div_sum += i // x
        div_sum -= i  # Exclude the number itself from the sum
        if div_sum > i:
            non_abund.append(i)
    return sum(non_abund)

if __name__ == "__main__":
    print(non_abundant())


