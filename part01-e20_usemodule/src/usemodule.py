#!/usr/bin/env python3
'''
well, do not import the same module twice. 
one of the debuggings of all time :)
'''
#import triangle
# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    #import triangle
    print(triangle.hypotenuse(3, 9))
    print(triangle.area(3,9))
    # Call the functions from here

if __name__ == "__main__":
    main()
