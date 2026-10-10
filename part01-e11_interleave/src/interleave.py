#!/usr/bin/env python3
'''
my code certainly ended up longer than the model
solution. the task page even suggested using extend to
unpack the tuples, but i intuitively leaned to use append. 
adding multiple at a time should be more efficient of course,
and nested looping wouldnt be required then.

so while i can see optimizations after completion. i will once
again not fix my "mistakes", but just read, learn, and gg go next.
'''
def interleave(*lists): #presumes equal length
    interleaved = []
    zipped = list(zip(*lists))#corrects the order. need to untuple the list next
    #list conversion here is unnecessary as zip returns an iterable, but print
    #statement use makes testing the code easier for me.
    #print(zipped)

    for tuple in zipped:
        for item in tuple:
            interleaved.append(item)
        
    return interleaved

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
