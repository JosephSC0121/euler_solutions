char_num_dict={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

def triangle_numbers(n):
    return {int(0.5 * i * (i + 1)) for i in range(1, n + 1)}
        
def coded_triangle_numbers():
    tn = triangle_numbers(35)
    count = 0
    for palabra in read_file():
        suma = 0
        for word in palabra:    
            suma += char_num_dict[word]
        if(suma in tn):
            count += 1
    return count

def read_file():
    with open("words.txt", "r", encoding="utf-8") as file:
        palabras = file.read().split(",")
    return [palabra.strip().replace('"', '').upper() for palabra in palabras]

print(coded_triangle_numbers())