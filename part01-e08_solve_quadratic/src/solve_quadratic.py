#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    discriminant = math.sqrt(b ** 2 - 4*a*c)
    x_1 = (-b + discriminant )/(2*a)
    x_2 = (-b - discriminant )/(2*a)
    #model just puts the above 2
    #formulas into the return statement
    return (x_1,x_2)


def main():
    print(solve_quadratic(1,-3,2))
    print(solve_quadratic(1,2,1))
    #print(solve_quadratic(1,2,99))
    #of course you should cover error-causing
    #inputs via raise or except
if __name__ == "__main__":
    main()
