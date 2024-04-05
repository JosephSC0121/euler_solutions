# Project Euler Problem #14

def collatz_sequence(num):
    count = 0
    aux = 0
    maxNum = 0 
    for n in range(num, 1, -1):
        current_num = n
        while n != 1:
            if n%2 == 0:
                n = n/2
                count += 1
            else:
                n = 3*n+1
                count += 1
        if count > aux:
            aux = count
            maxNum = current_num
        count = 0
    return maxNum

if __name__ == "__main__":
    num = 1000000
    print(collatz_sequence(num))

