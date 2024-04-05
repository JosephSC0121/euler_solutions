# Project Euler Problem #9
def pitagoras_triplet():
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                result = a*b*c
                break
    return result

if __name__ == "__main__":
    print(pitagoras_triplet()) 
