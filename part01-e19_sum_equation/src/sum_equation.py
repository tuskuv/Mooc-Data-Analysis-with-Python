#!/usr/bin/env python3
'''
in this one i had fun with realizing that you indeed should not be using
"sum" as the name your variable. :)

'''




def sum_equation(L):

    numbers_as_str = [str(number) for number in L]
    total = " + ".join(numbers_as_str)

    if total == "": #model just return "0 = 0" instead
        total = "0"

    total += f" = {sum(L)}"

    return total

def main():
    print(sum_equation([1, 5, 7]))
    pass

if __name__ == "__main__":
    main()
