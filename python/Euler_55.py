def lychrel_numbers():
    count = 0  

    for num in range(10000):
        is_lychrel = True  
        for _ in range(50):  
            num = num + int(str(num)[::-1])  
            if str(num) == str(num)[::-1]: 
                is_lychrel = False
                break
        
        if is_lychrel:
            count += 1  
    return count  

print(lychrel_numbers())
