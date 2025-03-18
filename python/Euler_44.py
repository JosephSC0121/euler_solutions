import math

def list_pentagon():
    lista = []
    for num in range(1, 10000):  
        pn = num * (3 * num - 1) // 2
        lista.append(pn)
    return lista

def verify(n):
    discriminant = 24 * n + 1
    if discriminant >= 0:
        sqrt_discriminant = math.isqrt(discriminant) 
        if sqrt_discriminant * sqrt_discriminant == discriminant and (1 + sqrt_discriminant) % 6 == 0:
            return True
    return False

def pentagon_number():
    pentagons = list_pentagon()  
    min_diff = float('inf')  

    for k in pentagons:
        for j in pentagons:
            if k > j and verify(k - j) and verify(k + j): 
                diff = abs(k - j)
                if diff < min_diff:
                    min_diff = diff
    return min_diff

print(pentagon_number())
