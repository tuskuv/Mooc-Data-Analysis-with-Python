#!/usr/bin/env python3
'''
well this was a fun 30 seconds to do.
at least this time the lambda was supposed
to be used.
'''
def positive_list(L):

    return list(filter(lambda x : x > 0, L))

def main():
    print(positive_list([2,-2,0,1,-7]))

if __name__ == "__main__":
    main()
