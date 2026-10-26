#!/usr/bin/env python3
'''
Ok this is kind of painful how my laptop takes 10 seconds
to run a test even with the smaller file iris2 to speed it up a bit, lol.
Otherwise this one was pretty simple to do.

surprisingly the model uses a transpose instead of rowvar=False
'''
import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    data_array = load()
    return scipy.stats.pearsonr(data_array[:,0], data_array[:,2])[0]

def correlations():
    data_array = load()
    #rowvar = False, observations are the rows.
    return np.corrcoef(data_array, rowvar=False)#np.array([])

def main():

    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
