#!/usr/bin/env python3
'''
Exercise 2.13 (diamond)
Create a function diamond that returns a two dimensional integer array where the 1s form a diamond shape. 
Rest of the numbers are 0. 
The function should get a parameter that tells the length of a side of the diamond. 
Do this using the eye and concatenate functions of NumPy and array slicing.

So the idea is to combine 4 2n-1 identity matrices and slice them appropriately.

I feel like this one was supposed to be easy, but i took a few days off so coming into this cold wasnt nice.
looots of print statements and testing was involved, but i got there somewhat smoothly despite not feeling
very focused on this task.

'''



import numpy as np

def diamond(n):

    i = np.eye(n, dtype=int)
    i_r = i[::-1]
   
    upper = np.concatenate((i_r, i[:,1:]), axis=1)
    lower = np.concatenate((i[:,:-1], i_r), axis=1)

    return np.concatenate((upper, lower[1:]), axis=0)





def main():
    pass


if __name__ == "__main__":
    main()
