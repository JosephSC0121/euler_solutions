# Project Euler Problem #35
import math
def prime_number(n):
    for i in range (2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def rotate_number(num,rotations):
    num_str = str(num)
    rotated_str = num_str[rotations:] + num_str[:rotations]
    rotated_num = int(rotated_str)
    return rotated_num

def circular_primes():
    aux = 0
    count = 0
    for i in range(2, 1000000):
        if prime_number(i):          
            for x in range (1, len(str(i))+1):
                rot_number = rotate_number(i,x)
                is_circular_prime = True and prime_number(rot_number)
                if prime_number(rot_number) == False:
                    break
            if is_circular_prime:
                count +=1
    return count


if __name__ == "__main__":
    print(circular_primes())
    


