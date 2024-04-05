from math import gcd
def phi(n):
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count += 1
    return count

def f(n):
    acc = 0
    for i in range(1, n+1):
        acc += phi(n**i)
    res = acc % (n+1)

    return res

def g(n):
    add = 0
    for i in range(1, n+1):
        add += f(i)
    return add

if __name__ == "__main__":
    print(g(8))
