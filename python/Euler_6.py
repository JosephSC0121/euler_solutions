# Project Euler Problem #6
# the sum of the squares

def sum_squares(num):
    return sum([i**2 for i in range(1, num+1)])

#The square of the sum 

def square_sum(num):
    result = (sum([i for i in range(1, num+1)]))**2
    return result    

if __name__ == "__main__":
    num = 100
    print(square_sum(num) - sum_squares(num))
    
