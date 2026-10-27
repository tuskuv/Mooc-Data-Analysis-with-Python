#!/usr/bin/env python3
'''
model solution:
def subfigures(a):
    fig, ax = plt.subplots(1,2, figsize=(6,3))
    ax[0].plot(a[:,0], a[:,1])
    ax[1].scatter(a[:,0], a[:,1], c=a[:,2], s=a[:,3])
    plt.show()
quite different from mine. the materials showcased 2 different
approaches so i guess there nohing wrong with mine.
'''
import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):

    colors = a[:,2]

    sizes = a[:,3]

    plt.subplot(1, 2, 1)
    plt.plot(a[:,0], a[:,1])

    plt.subplot(1, 2, 2)
    plt.scatter(a[:,0], a[:,1], c = a[:,2], s = a[:,3])

    plt.show()




def main():
    subfigures(np.array([[1, 2, 3, 4], [5, 3, 7, 5], [7, 1, 1, 5], [2, 3, 4, 5]]))

if __name__ == "__main__":
    main()
