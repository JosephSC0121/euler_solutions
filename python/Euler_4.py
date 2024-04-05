# Project Euler Problem #4

def palindrome():
    maxNum = 0 
    for x in range(999,100,-1):
        for i in range(999,100,-1):        
            aux = x*i 
            str_num = str(aux)
            if str_num == str_num[::-1] and aux > maxNum:
                maxNum=aux       
    return maxNum               
if __name__ == "__main__":
    print(palindrome())

 


