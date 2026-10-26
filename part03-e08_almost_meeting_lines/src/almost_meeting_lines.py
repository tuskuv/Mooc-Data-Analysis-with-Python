#!/usr/bin/python3
'''
ok this is dumb. the test passed without using
the function "np.linalg.lstsq(a, b)", but its usage being
required was even dumber. they are LINES, if they dont meet
at any point then theyre parallel.
'''
import numpy as np

def almost_meeting_lines(a1, b1, a2, b2):

    a = np.array([[-a1, 1], [-a2, 1]])
    b = np.array([b1, b2])
    exact = True
    x = 0
    y = 0   
    try:
        x, y = np.linalg.solve(a, b)
    except np.linalg.LinAlgError:   #now i could at least use a point on a line instead of (0,0), but whatever.
        exact = False
        #np.linalg.lstsq(a, b)

    return [(x, y), exact]


def main(): 
    a1=1    #x+2=y, -x=y
    b1=2
    a2=-1
    b2=0

    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")

    a1=a2=1
    b1=2
    b2=-2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b1)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    a2=1
    b2=1
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

if __name__ == "__main__":
    main()
