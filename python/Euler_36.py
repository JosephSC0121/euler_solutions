# Project Euler Problem #36

def palindrome():
    sumNum = 0 
    for x in range(0,1000001):
            str_num = str(x)
            if str_num == str_num[::-1]:
                numero_binario = bin(x)[2:]
                binario_str = str(numero_binario) 
                if numero_binario == binario_str[::-1]:                      
                        sumNum += x
    return sumNum
if __name__ == "__main__":
    print(palindrome())

 



