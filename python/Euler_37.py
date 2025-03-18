import math 
def remove_digits_l_r(num):
    num_str = str(num) 
    lista = []
    for i in range(len(num_str)):
        lista.append(int(num_str[i:]))
    return lista
    

def remove_digits_r_l(num):
    num_str = str(num) 
    lista = []
    for i in range(len(num_str), 0, -1):
        lista.append(int(num_str[:i]))
    return lista
        
def prime_number(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n% i == 0:
             return False
    return True

def truncable_primes():
    lista = []
    for i in range(100, 10, -1): 
        if prime_number(i):           
            left_truncatable = all(prime_number(x) for x in remove_digits_l_r(i))
            right_truncatable = all(prime_number(x) for x in remove_digits_r_l(i))
            if left_truncatable and right_truncatable:
                lista.append(i)
    return lista


print(truncable_primes())        
   
            