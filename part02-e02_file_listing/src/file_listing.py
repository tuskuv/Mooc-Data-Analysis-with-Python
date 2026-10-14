#!/usr/bin/env python3
'''
looking at the format, we are interested only in stuff after the text
"jttoivon hyad-all" (yes, hardcoding this is bad practice)

so original plan was:
use findall to create a list of target strings
loop for line in list
    use .split() to separate the column values
    create a tuple consisting of these values
which i just naturally didnt do and forgot all about.

this was a fun excercise to do as well, i enjoyed it.

'''

import re

def file_listing(filename="src/listing.txt"):

    list_of_strings : list = [] #this could probably be skipped, but ill keep the step
    list_of_tuples : list = []
    with open(filename, "r") as myfile: #the regex would more optimally be applied with the file open, but i did the excercise in a "safe" order instead.
        for line in myfile:
            list_of_strings.append(line.strip())

    #i=0
    for line in list_of_strings:
        tuplematch = re.search(r'hyad-all\s+(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s+(\w*.[\w-]+.[\w-]*)', line).groups()
        #above the final "capture group"? might not be optimal, but it worked on the given data set.


        #i used a counter here to check for spots the regex ran into a issues.
        #print(tuplematch)
        #if i > 5: 
        #    break
        #i += 1

        #this felt a bit silly, but it was the lazy was to make some columns type int after the fact.
        #surprised to the see model did basically the same thing here.
        tuplematch_inted = (int(tuplematch[0]), tuplematch[1], int(tuplematch[2]), int(tuplematch[3]), int(tuplematch[4]), tuplematch[5])
        list_of_tuples.append(tuplematch_inted)



    return list_of_tuples
    #return a list of tuples (size, month, day, hour, minute, filename)



def main():
    file_listing("src/listing.txt")
if __name__ == "__main__":
    main()
