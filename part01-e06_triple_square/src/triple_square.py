#!/usr/bin/env python3
'''
its interesting how different this course is to mooc python.
i expected everything in ch. 1 to be "old news", but quite 
a bit of the syntax presented is fresh to me.
".format(i, t, s)" is something im not used over
using f" " f-strings.
'''

def triple(multipliable):
    return 3*multipliable


def square(squarable):
    return squarable**2


def main():
    #for i in range(1, 11):
    #    print(f"triple({i})=={triple(i)} square({i})=={square(i)}")
    #part 2 asked to modify above loop that completed part 1. not a fan of this structure. just have it be in a different excercise instead.
    for i in range(1, 11):
        sq = square(i)
        tr = triple(i)
        if sq > tr:
            break
        print(f"triple({i})=={tr} square({i})=={sq}")
        #print("triple({0})=={1} square({0})=={2}".format(i, t, s))

if __name__ == "__main__":
    main()
