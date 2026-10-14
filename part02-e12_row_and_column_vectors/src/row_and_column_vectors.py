#!/usr/bin/env python3
'''
this is new stuff for me, so my answers should be leaving room for improvement.
here the model used a.shape vs my use of len(a), same output at least.

anyways i find it odd how .shape[] doesnt yield ctrl+f results in the 
study materials. quite a bit of text i read and in the end i was expected to
use something not really taught.

but anyways, passed first try with my intuitive solution.
'''
import numpy as np

def get_row_vectors(a):
    #for row in a:
    return np.split(a, len(a))

def get_column_vectors(a):

    return np.split(a, len(a[0]), axis=1)
    #return np.split(a, a.shape[1], axis=1)

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    #print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
