#!/usr/bin/env python3
'''
this was the first task that was a little challenging, and
it ended up being one of those where you try to tweak the
code to get to the correct result bit by bit. model solution
doesnt use a helper function as i did and seems better. now the resulted 
code isnt great, but im not going spend time making it readable or efficient.
maybe its bad to be "lazy" like this, but i want to move on
after collecting the mooc points.

'''

def gather_range(L):
    e : int = 0
    for i in range(len(L)): #i from 0 to len
        if i >= len(L) - 1:
            break   #if i is last item on the list, we are done
        if L[i] + 1 == L[1+i]:
            e += 1
        else:
            break   #if increment not 1, we are done.
    if e > 0:
        return (L[0], L[e]+1)
    return L[0]

def detect_ranges(L):
    L = sorted(L)
    print(L)
    i = 0
    ranged = []
    while i < len(L):
        rangepair_or_single = gather_range(L[i:])
        if type(rangepair_or_single) is int:
            i += 1
        else:
            i += rangepair_or_single[1]-rangepair_or_single[0]
        ranged.append(rangepair_or_single)

    return ranged





def main():
    L = [2, 2, 2, 3, 4] #my approach works with lists containing
                        #duplicates, although it wasnt required in the task.
    result = detect_ranges(L)
    #print(L)
    print(result)

if __name__ == "__main__":
    main()
