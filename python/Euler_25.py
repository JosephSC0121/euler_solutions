# Project Euler Problem #25
def index_fibonacci():
    fib1=1 
    fib2=1
    count = 2
    index = 0

    while index < 1000:
        nFib = fib1 + fib2
        count += 1
        index = len(str(nFib))
        fib1 = fib2
        fib2 = nFib
    return count

if __name__ == "__main__":
    print(index_fibonacci())


