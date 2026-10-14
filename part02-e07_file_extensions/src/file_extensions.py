#!/usr/bin/env python3
'''
felt like a chore, got there though.
the model solution used split instead of regex which is probably better, but
i think i need more practice with regex anyways so im ok with being "wrong" here.
'''
import re


def file_extensions(filename):

    filenames : list = []   #this name is poor because i originally thought i was to pick up all filenames rather than extensionless ones only
    extention_dict : dict = {}
    pattern = r"(\w*)\W(\w+)$"
    #first capture group catches everything before first alphanumeric
    #2nd group catches everythin after last alphanumeric
    with open(filename, "r") as myfile:
        for line in myfile:
            line = line.strip()
            try:
                file_name, extention = re.search(pattern, line).groups()
            except AttributeError:  #if no non-alphanumeric is found, we get here
                filenames.append(line)
                continue

            if extention not in extention_dict:
                extention_dict[extention] = [line]
            else:
                pass
                extention_dict[extention].append(line)

    return (filenames, extention_dict)
    #The function should return a pair, where the first element is a list containing all filenames with no extension (with the preceding period (.) removed). 
    # The second element of the pair is a dictionary with extensions as keys and corresponding values are lists with filenames having that extension.

def main():
    pass
    result = file_extensions("src/filenames.txt")
    print(f"{len(result[0])} files with no extension")
    for key, values in result[1].items():
        print(f"{key} {len(values)}")



if __name__ == "__main__":
    main()
