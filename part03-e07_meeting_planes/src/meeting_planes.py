#!/usr/bin/python3
'''
this was pretty much the same excercise again.
took a couple to tries because i had a typo somewhere?
im not what i even fixed but the tests passed the test after
some order changing.
'''
import numpy as np

#ModuleNotFoundError: No module named 'numpy.linalg.linalg'
import numpy.linalg
numpy.linalg.linalg = numpy.linalg
#also this time i had to edit the test module as well
#this course is a bit outdated, so i guess updates can break stuff and no one will ever fix things anymore.

def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):

    #z = a1y+b1x+c

    #-b1x-a1y+z = c1

    a = np.array([[-b1, -a1, 1], [-b2, -a2, 1], [-b3, -a3, 1]])
    #fixed the order here compared to the previous one.
    b = np.array([c1, c2, c3])
    x, y, z = np.linalg.solve(a, b)
    return x, y, z



def main():
    a1=1
    b1=4    
    c1=5
    a2=3
    b2=2
    c2=1
    a3=2
    b3=4
    c3=1

    x, y, z = meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    print(f"Planes meet at x={x}, y={y} and z={z}")

if __name__ == "__main__":
    main()
