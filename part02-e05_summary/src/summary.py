#!/usr/bin/env python3
'''
did not have fun with this one, not used to writing 
in the terminal which might be a very bad thing.
'''
import sys
import math

def sd(numbers, average):
    #helper function. sure, i couldve just done this inside summary.
    numbers_minus_avg_squared = list(map(lambda x : (x-average)**2, numbers))


    return math.sqrt(sum(numbers_minus_avg_squared)/(len(numbers)-1))


def summary(filename):

    numbers = []
    
    with open(filename, "r") as myfile:
        for line in myfile:
            try:
                numbers.append(float(line.strip()))
            except ValueError:
                continue

    total_value = sum(numbers)
    average = total_value/len(numbers)
    standard_deviation = sd(numbers, average)

    return (total_value, average, standard_deviation)  #a triple containing the sum, average, and standard deviation


def main():
    for example in sys.argv[1:]:
        values = summary(example)
        print(f"File: {example} Sum: {values[0]:.6f} Average: {values[1]:.6f} Stddev: {values[2]:.6f}")

if __name__ == "__main__":
    main()
