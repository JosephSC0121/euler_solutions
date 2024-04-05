# Project Euler Problem #31
import time
def coins(): 
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * 201
    ways[0] = 1

    for coin in coins:
        for i in range(coin, 201):
            ways[i] += ways[i - coin]

    return ways[200]

if __name__ == "__main__":
    start = time.time()
    print(coins())
    end = time.time()
    print(end - start)
