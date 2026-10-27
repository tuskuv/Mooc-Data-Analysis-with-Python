#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def main():
    #The first graphs has x coordinates 2,4,6,7 and y coordinates 4,3,5,1. 
    a_x = np.array([2,4,6,7])
    a_y= np.array([4,3,5,1])

    # The second graph has x coordinates 1,2,3,4 and y coordinates 4,2,3,1.
    b_x = np.array([1,2,3,4])
    b_y = np.array([4,2,3,1])

    #model: plt.plot([2,4,6,7], [4,3,5,1], [1,2,3,4], [4,2,3,1])

    plt.title("09 multiple graphs")
    plt.xlabel("x-axis label") 
    plt.ylabel("y-axis label") 
    plt.plot(a_x, a_y, color='blue')

    plt.plot(b_x, b_y, color='red')

    plt.show() 

if __name__ == "__main__":
    main()
