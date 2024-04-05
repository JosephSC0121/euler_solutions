# Proyect Euler Problem #21
import numpy as np
def amicable(end):
    start = 1
    end += 1
    amicables = []
    numbers = np.arange(start, end)
    modules = np.zeros(end, dtype=np.int_)

    # find and save in modules the modules of each number
    for x in np.nditer(numbers):
        module = np.where(x % numbers == 0)
        module_nums = numbers[module]
        module_sum = np.sum(module_nums)-x
        modules[x] = module_sum

    # Find the same modules and their position and then clean
    # the amicable numbers for not repeat.
    for x in np.nditer(numbers):
        left = modules[x]

        if left > end:
            continue

        right = modules[left]

        if right > end:
            continue

        if (modules[left] == right and
            modules[right] == left and
                left != right):
            amicables.append(left)
            amicables.append(right)
            modules[left] = 0
            modules[right] = 0
    return sum(amicables)
if __name__ == "__main__":
   print(amicable(10000))
    
    

