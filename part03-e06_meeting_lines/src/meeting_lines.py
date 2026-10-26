#!/usr/bin/python3
'''
fixing tech issues is not very fun.
and looking at the model, my code shouldve indeed
been passing without a hitch.
'''
import numpy as np

#ai suggested these imports just to get around
#"module 'numpy.linalg' has no attribute 'linalg'"
#code works without them though.
import numpy.linalg
numpy.linalg.linalg = numpy.linalg

def meeting_lines(a1, b1, a2, b2):

    #y=a1x+b1, y=a2x+b2
    
    # 1y - a1x = b1
    # 1y - a2x = b2

    a = np.array([[1, -a1], [1, -a2]])
    #mixed up x and y here, -a1, 1 wouldve been better
    b = np.array([b1, b2])
    y, x = np.linalg.solve(a, b)
    return x, y


def main():
    a1=1
    b1=4
    a2=6
    #b2=2
    b2=0
    x, y  = meeting_lines(a1, b1, a2, b2)
    print(f"Lines meet at x={x} and y={y}")

if __name__ == "__main__":
    main()
