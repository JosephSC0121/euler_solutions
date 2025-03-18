# import numpy as np

# def generar_matriz_espiral(n):
#     matriz = np.zeros((n, n), dtype=int)
#     x, y = n // 2, n // 2  
#     num = 1
#     pasos = 1  
#     direccion = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
#     d = 0  
    
#     matriz[x, y] = num
#     num += 1
    
#     while num <= n * n:
#         for _ in range(2): 
#             for _ in range(pasos):
#                 x += direccion[d][0]
#                 y += direccion[d][1]
                
#                 if 0 <= x < n and 0 <= y < n:
#                     matriz[x, y] = num
#                     num += 1
                
#                 if num > n * n:
#                     break
#             d = (d + 1) % 4  
#         pasos += 1  
    
#     return matriz


# matriz_espiral = generar_matriz_espiral(n)


# def summatrix():
#     suma  = 0
#     for i in range(0, n // 2 ):
#         print(matriz_espiral[i][i])
#         suma += matriz_espiral[i][i]
        
#     for x in range(n-1, n // 2, -1):
#         print(matriz_espiral[x][x])
#         suma += matriz_espiral[x][x]
        
#     for k in range(n // 2 +1, n):
#         print(matriz_espiral[k][(n-1)-k])
#         suma += matriz_espiral[k][(n-1)-k]
    
#     for j in range(n // 2, n):
#         print(matriz_espiral[n-1-j][j])
#         suma += matriz_espiral[n-1-j][j]
    
#     print(suma)        
# summatrix() 
 
import numpy as np

def generar_matriz_espiral(n):
    matriz = np.zeros((n, n), dtype=int)
    x, y = n // 2, n // 2 
    num = 1
    pasos = 1  
    direccion = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
    d = 0  
    
    matriz[x, y] = num
    num += 1
    
    while num <= n * n:
        for _ in range(2): 
            for _ in range(pasos):
                x += direccion[d][0]
                y += direccion[d][1]
                
                if 0 <= x < n and 0 <= y < n:
                    matriz[x, y] = num
                    num += 1
                if num > n * n:
                    return matriz 
            d = (d + 1) % 4 
        pasos += 1  

    return matriz

def summatrix(matriz):
    n = matriz.shape[0]
    suma = 0

   
    for i in range(n):
        suma += matriz[i, i]  
        if i != n - 1 - i:
            suma += matriz[i, n - 1 - i]  

    print("Suma de las diagonales:", suma)
    return suma


n = 5  
matriz_espiral = generar_matriz_espiral(n)
print(matriz_espiral)
summatrix(matriz_espiral)
