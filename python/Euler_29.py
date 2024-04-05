# Project Euler Problem #29
import numpy as np
def combinations():
    array = np.array([i ** x for i in range(2, 101) for x in range(2, 101)])
    return (np.unique(array)).size

if __name__ == "__main__":
     print(combinations())
