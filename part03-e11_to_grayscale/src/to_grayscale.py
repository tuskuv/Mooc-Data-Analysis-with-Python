#!/usr/bin/env python3
'''
its very frustrating when the computer keeps freezing and input lag is massive.
took some time to figure out how to do part 1, but part 2 was free at least.
'''
import numpy as np
import matplotlib.pyplot as plt


def to_grayscale(im):
    #(368, 640, 3) shape. height y, width x, color rgb
    #we want to reshape(368, 640)
    weights = [0.2126, 0.7152, 0.0722]

    temp = np.multiply(im, weights) #rgb weighted, now need to collapse color to 1d.

    result = np.sum(temp, axis = 2) #already weighted. just sum.  

    return result

def to_red(im):
    weights = [1, 0, 0]
    return np.multiply(im, weights)
def to_blue(im):
    weights = [0, 0, 1]
    return np.multiply(im, weights)
def to_green(im):
    weights = [0, 1, 0]
    return np.multiply(im, weights)
#   image2=image.copy()
#   image2[:,:,[1,2]] = 0
#the model solution sets to 0 instead of multiplying with 0, which should be better indeed.

def main():
    painting=plt.imread("src/painting.png")

    modified = to_grayscale(painting)
    plt.set_cmap('gray')
    plt.imshow(modified)
    
    plt.subplot(3, 1, 1)
    plt.imshow(to_red(painting))

    plt.subplot(3, 1, 2)
    plt.imshow(to_green(painting))

    plt.subplot(3, 1, 3)
    plt.imshow(to_blue(painting))
    
    plt.show()




if __name__ == "__main__":
    main()
