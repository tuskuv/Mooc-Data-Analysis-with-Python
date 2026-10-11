'''
this is a module for checking some triangle properties:
hypotenuse
area
'''


from math import sqrt

__version__ = "1.0.0"
__author__ = "uuh, me! im the author yay"

def hypotenuse(a, b):
    '''
    calculates hypoenuse of a triangle defined by
    given 2 cathetus arguments
    '''
    return sqrt(a ** 2 + b ** 2)

def area(a, b):
    '''
    calculates area of a triangle defined by
    given 2 cathetus arguments
    '''
    return a*b/2




def main():
    pass
    print(hypotenuse(3, 4))
    print(area(3, 4))
if __name__ == "__main__":
    main()