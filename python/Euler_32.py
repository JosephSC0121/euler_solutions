def pandigital_products():
    lista_buenos = set() 
    
    for x in range(1, 100): 
        for i in range(100, 10000 // x): 
            combinacion = str(x) + str(i) + str(x * i)
            if len(combinacion) == 9 and set(combinacion) == set("123456789"):
                print(x,i, x*i)
                lista_buenos.add(x * i)  
          
    return sum(lista_buenos)

print(pandigital_products())
