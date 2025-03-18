def integer_right_triangles():
    max_count = 0
    for i in range(1000, 0, -1):
        if max_count < pythagorean(i):
            max_count = pythagorean(i)
            print(i)
    return max_count

def pythagorean(p):
    count = 0
    for a in range(1, p // 3):
        for b in range(a, (p-a) // 2):
            c = p - a - b
            if a * a + b * b == c * c:
                count += 1
    return count


integer_right_triangles()