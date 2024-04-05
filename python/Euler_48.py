# Euler Project Problem 48

def self_powers():
    sum = 0
    for i in range(1, 1001):
        sum += i**i
    return str(sum)[-10:]

if __name__ == "__main__":
    print(self_powers())
