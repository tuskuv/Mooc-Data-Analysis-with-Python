#!/usr/bin/env python3
'''
matrix powers

looking at the model solution i made a meal of this by messing with lambda expressions again.
i even wrote function to with the reduce but scrapped it when something else ended up not working.
not very comfortable with the reduce function and the idea of generators, 
but that should change over time.
'''
from functools import reduce
import numpy as np

def matrix_power(a, n):
    if np.linalg.det(a) == 0:  #rounding issues with floats may need fixing.
        return "a is a non invertible matrix"

    a_eye = np.eye(len(a[0]))   #an identity matrix matching a:s dimensions
    if n == 0:
        return a_eye
    if n < 0:
        a = np.linalg.inv(a)
        n = -n  #turns out range(-n) is not a thing

    #function(startpoint, power) return startpoint*a (**power)
    a_pow = reduce(lambda a_eye, n: a_eye @ a, range(n), a_eye)
    return a_pow


def main():
    #np.random.seed(0)
    a=np.array([1, 2, 3, 4]).reshape(2,2)
    #a=np.random.randint(1,5, (2,2))
    print(matrix_power(a, -3))

if __name__ == "__main__":
    main()
