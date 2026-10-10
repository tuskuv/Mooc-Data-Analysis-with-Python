#!/usr/bin/env python3
'''
list comprehensions and generators are something im familiar with. 
and while they arent hard to read i have gotten used to "normal" structures. 

so id guess instead of directly using a list comprehension i will be doing 
normal structures and then transforming them to list comprehensions to optimize 
the code(at leaast when its required).

and optimization will probably feel important when working big data sets later
'''
def exerc_5():
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == 5:
                print(f"({i}, {j})")



def main():
    #model solution used:
    #print("\n".join(f"({a},{b})" for a in range(1, 7) for b in range(1, 7) if a + b == 5))
    
    #my failure was not thinking about concatenating or joining the tuple into a singular string.
    G =( (i, j) for i in range(1,7) for j in range(1,7)  if i+j == 5)

    for item in G:  #idk why the autoreview let me pass, but ok.
        print(item)

if __name__ == "__main__":
    main()
