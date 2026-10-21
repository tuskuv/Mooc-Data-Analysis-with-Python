#!/usr/bin/env python3
'''
i guess this is slower, but with math background transposing feels more intuitive than slicing.
'''
import numpy as np

def column_comparison(a):

    a_transpose = np.transpose(a)

    c = a_transpose[1] > a_transpose[-2]
    #vs model: c = a[:,1] > a[:,-2]

    return a[c]
    
def main():
    b=np.array([[8, 9, 3, 8, 8],
    [0, 5, 3, 9, 9],
    [5, 7, 6, 0, 4],
    [7, 8, 1, 6, 2],
    [2, 1, 3, 5, 8]])

    print(column_comparison(b))

if __name__ == "__main__":
    main()
