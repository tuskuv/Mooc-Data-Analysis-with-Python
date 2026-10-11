#!/usr/bin/env python3
'''
You have to use split, map, and zip functions/methods.

working up from the bottom, the amount of code lines could 
clearly be reduced. replace the bottom paired with
list(zip(s1.split(), s1.split())), but its still very different
from the model solution. i was quite uncomfortable trying to force
the map function into the program when the task was easy to do
without it. even the model solution doesnt look like it should use map.
'''



def transform(s1, s2):
    words_1 = s1.split()
    words_2 = s2.split()

    paired = list(zip(words_1, words_2)) 

    #print(paired) prints list of string doubles

    #map each tuple into the product? yes:
    multiplied = list(map(lambda tuple : int(tuple[0])*int(tuple[1]), paired))
    #print(multiplied)
    return multiplied

    #model:
    #return [ a*b for (a, b) in zip(map(int, s1.split()), map(int, s2.split())) ]

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
