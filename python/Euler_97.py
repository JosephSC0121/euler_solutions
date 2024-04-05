if __name__ == "__main__":
    aux = 2**7830457 * 28433 +1
    last_digits = aux % 10 ** 10 
    print(last_digits)
