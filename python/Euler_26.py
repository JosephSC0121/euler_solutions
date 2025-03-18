def reciprocal_cycles():
    max_length = 0
    max_number = 0
    
    for i in range(2, 1000): 
        if i % 2 != 0 and i % 5 != 0:
            remainder = 1
            position = 0
            seen = {}
            
            while remainder not in seen:
                seen[remainder] = position
                remainder = (remainder * 10) % i
                position += 1
                
                if remainder == 0:  
                    position = 0
                    break
            
            if position > max_length:
                max_length = position - seen[remainder]
                max_number = i
  
    return max_number

print(reciprocal_cycles())