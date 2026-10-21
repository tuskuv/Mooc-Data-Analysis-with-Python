#!/usr/bin/env python3
'''
got a bit stuck because i had "cosines.clip()" instead of "clip(cosines)"
'''
import numpy as np
import scipy.linalg

def vector_angles(X, Y):

    numerator = np.sum(X*Y, axis = 1)

    denom = scipy.linalg.norm(X, axis=1)*scipy.linalg.norm(Y, axis=1)

    cosines = numerator / denom

    radangles = np.arccos(np.clip(cosines, -1, 1))

    degangles = radangles*180/np.pi

    return degangles

def main():
    a=np.array([[1,0,0], [4,5.1,1]])
    b=np.array([[0,1,0], [1,1,4]])
    print(vector_angles(a, b))

if __name__ == "__main__":
    main()
