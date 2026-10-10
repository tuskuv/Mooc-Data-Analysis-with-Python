#!/usr/bin/env python3
'''
this is one where reading the objective wouldve been a great idea.
nonetheless it was easy despite me first coding for the output
{'o': 3, 'y': 1, 'r': 1, 'c': 2, 't': 1, 'l': 1, 'h': 1, 'e': 1, 'p': 2, 'k': 2}.
oops.

'''
def distinct_characters(L):
    string_char_quantities = {}

    for string in L:
        quantity = len(set(string))
        string_char_quantities[string] = quantity

    return string_char_quantities

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))


if __name__ == "__main__":
    main()
