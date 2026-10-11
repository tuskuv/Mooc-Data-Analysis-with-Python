#!/usr/bin/env python3
'''
regex is something i have found useful even before learning the syntax so
i like being forced to get used to it. my solution here is awful, but it
works and used regex at least. this will take some time to get used to

'''
import re

def integers_in_brackets(s):

    matches = re.findall(r"(.[-+]?\b\d+) *\]", s)

    print(matches)
    printout = []
    for match in matches:
        if match[0] in r"[\[\(\{ ]":
            if match[1] == "+":
                printout.append(int(match[2:]))
            else:
                printout.append(int(match[1:]))

    return printout

def main():
    #pass
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"))
    #print(integers_in_brackets(" afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx!"))

if __name__ == "__main__":
    main()
