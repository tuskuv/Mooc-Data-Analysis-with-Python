#!/usr/bin/env python3
'''
part 2 was now easy because of doing the same thing in the last exercise.
part 1 immediately worked without an error even in testing too.
'''
import sys

def file_count(filename):
    linecount : int = 0
    wordcount : int = 0
    charcount : int = 0
    with open(filename, "r") as myfile:
        for line in myfile:
            linecount += 1
            charcount += len(line)
            wordcount += len(line.split())

    return (linecount, wordcount, charcount)
#The function should read the file, count the number of lines, words, and characters in the file, and return a triple with these count in this order.





def main():
    #print(file_count("src/test.txt"))
    i = 0
    for file in sys.argv[1:]:
        triple_values = file_count(file)
        print(f"{triple_values[0]}\t{triple_values[1]}\t{triple_values[2]}\tfile{i}")
        i += 1

if __name__ == "__main__":
    main()
