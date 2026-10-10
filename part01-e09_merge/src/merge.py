#!/usr/bin/env python3
'''
so sorting but not allowed to use sort or sorted?
since the input lists are sorted, i shall
look into comparing the first elements one
by one.

using "extend" was somehow new to me, but
it was very intuitive.
'''
def merge(L1, L2):
    L = []
    limit1 = len(L1)
    #using limit1 and 2 makes sense imo to avoid calling
    #the len function over and over again as the model does.
    limit2 = len(L2)
    
    i = 0
    j = 0
    while i < limit1 and j < limit2 :
        if L1[i] <= L2[j]:
            L.append(L1[i])
            i += 1
        else:
            L.append(L2[j])
            j += 1
    if i < limit1:
        L.extend(L1[i:])
    if j < limit2:
        L.extend(L2[j:])
    return L

def main():
    A = [12, 2, 3]
    B = [-1, 1, 5, 2, 13, 13, 13]
    print(merge(sorted(A), sorted(B)))

if __name__ == "__main__":
    main()
