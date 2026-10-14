#!/usr/bin/env python3
'''
this was even easier than the previous one
'''
import re

def red_green_blue(filename="src/rgb.txt"):
    colors = []
    with open(filename, "r") as myfile:
        next(myfile)
        i=0
        for line in myfile:

            placeholder = re.search(r"\s*(\d+)\s+(\d+)\s+(\d+)\s+([\w]+[\w\s]+)", line.strip()).groups()

            colors.append(f"{placeholder[0]}\t{placeholder[1]}\t{placeholder[2]}\t{placeholder[3]}")


    #'255\t250\t250\tsnow' return a list of strings at this format
    return colors


def main():
    red_green_blue()
if __name__ == "__main__":
    main()
