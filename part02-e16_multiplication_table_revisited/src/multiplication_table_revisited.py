#!/usr/bin/env python3
'''
Write function multiplication_table that gets a positive integer n as parameter. 
The function should return an array with shape (n,n). 
The element at index (i,j) should be i*j. 
Don't use for loops! In your solution, rely on broadcasting, the np.arange function, reshaping and vectorized operators. 

Expected the final task of this set to be trickier, but it took me about 2 seconds.
'''
import numpy as np

def multiplication_table(n):
    
    a=np.arange(n)
    b=np.arange(n).reshape((n,1))
    
    
    return a*b

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
