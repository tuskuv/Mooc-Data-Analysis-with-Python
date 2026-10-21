#!/usr/bin/env python3
'''
Write function first_half_second_half that gets a two dimensional array of shape (n,2*m) as a parameter. 
The input array has 2*m columns. 
The output from the function should be a matrix with those rows from the input that have the sum of the first m elements larger than the sum of the last m elements on the row. 
Your solution should call the np.sum function or the corresponding method exactly twice.

the model solution properly split the matrix in half which is more intuitive, but
i think im supposed to default to slicing more often so i used slicing.
'''
import numpy as np

def first_half_second_half(a):
    halfway = int(len(a[0])/2)

    c = np.sum(a[:, :halfway], axis=1) > np.sum(a[:,halfway:], axis=1)

    return a[c]

def main():
    pass
    b=np.array([[8, 9, 3, 8, 8, 1],
    [0, 1, 5, 3, 9, 9],
    [5, 4, 7, 6, 0, 4],
    [7, 8, 1, 5, 6, 2],
    [2, 1, 3, 5, 2, 8]])
    print(first_half_second_half(b))


if __name__ == "__main__":
    main()
