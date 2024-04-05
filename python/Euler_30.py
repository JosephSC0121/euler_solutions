# Euler Project Problem 30 

def fifth_powers():
    numbers = []
    for i in range(2, 1000000):
        aux = str(i)
        result = 0
        for digit in aux:
            result += (int(digit)**5)
        if result == i:
            numbers.append(i)
    return sum(numbers)

if __name__ == "__main__":
    print(fifth_powers())

        

