#!/usr/bin/env python3
'''
Write function vector_lengths that gets a two dimensional array of shape (n,m) as a parameter. 
Each row in this array corresponds to a vector. 
The function should return an array of shape (n,), that has the length of each vector in the input. 
The length is defined by the usual Euclidean norm (Wikipedia). 
Don't use loops at all in your solution. Instead use vectorized operations. 
You must use at least the np.sum and the np.sqrt functions. 
You can't use the function scipy.linalg.norm. 
Test your function in the main function.

this is one of those where you swear you did what the model solution did, 
but it didnt work so you looked for an alternative solution.

i dont want to talk about it. moving on.
'''
import numpy as np


def vector_lengths(a):

    sums = np.sum(a**2, axis=1, keepdims=True)
    vlens = np.sqrt(sums)
    result = np.ravel(np.array(vlens))

    return np.ravel(np.array(np.sqrt(np.sum(a**2, axis=1, keepdims=True))))
    #return np.sqrt(np.sum(a**2, axis=1))

def main():
    pass
    b=np.array([[1,2,3], [4,5,6]])
    print(vector_lengths(b))

if __name__ == "__main__":
    main()
