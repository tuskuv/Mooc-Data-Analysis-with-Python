#!/usr/bin/env python3

import numpy as np

def column_comparison(a):

    a_transpose = np.transpose(a)
    print(a)
    print(a_transpose)
    c = a_transpose[1] > a_transpose[-2]
    print(c)

    return a[c]
    
def main():
    pass
    #a=np.array([[1,22,9,4], [2,9,8,7], [2,53,7,6]])
    b=np.array([[8, 9, 3, 8, 8],
 [0, 5, 3, 9, 9],
 [5, 7, 6, 0, 4],
 [7, 8, 1, 6, 2],
 [2, 1, 3, 5, 8]])

    print(column_comparison(b))

if __name__ == "__main__":
    main()
