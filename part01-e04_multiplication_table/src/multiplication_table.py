#!/usr/bin/env python3
'''i tend to prioritize readability when doing
excercises as long the efficency doesnt suffer
too much, so using an extra variable here or 
there will be common.'''

def main():
    for i in range(1, 11):
        for j in range(1, 11):  
            #model solution uses: print(f"{r*c:4d}", end="")
            product : str = "{:4d}".format(i*j)
            print(product, end="")
        print("")

if __name__ == "__main__":
    main()
