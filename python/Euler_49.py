from itertools import permutations
import math 
def prime_number(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n% i == 0:
             return False
    return True

def prime_permutations():
    
    for i in range(2000,10000):
        lista = []
        if prime_number(i):
            lista.append(i)
            for number in permutations(str(i)):
                aux = int(''.join(number))
                if((aux - i) == 3330 or (aux - i) == 6660): 
                    if(prime_number(aux)):
                        lista.append(aux)   
                        if(len(lista) == 3):
                            return lista
    return lista

print(prime_permutations())

