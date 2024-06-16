def even_fibonacci_sum(limit):
    a, b = 2, 8
    total_sum = a
    while b <= limit:
        total_sum += b
        a, b = b, 4 * b + a
    return total_sum

if __name__ == "__main__":
    print(even_fibonacci_sum(4000000))
