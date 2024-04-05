# Project Euler Problem #40
def Champernownes():
    constant = "0"
    up = 1000000
    for i in range(1,up+1):
        constant += str(i)
    return constant
def prod():
    i=1
    result = 1
    for x in range(1, 8):
        result *= int(Champernownes()[i])
        i *= 10
    return result

if __name__ == "__main__":
    print(prod())

        

