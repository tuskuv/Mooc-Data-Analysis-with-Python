#!/usr/bin/env python3
'''
expected issues with this one, but no. smooth sailing. everything just worked intuitively.
'''
def word_frequencies(filename):
    
    freq = {} #key/value, word/frequency. case sensitivity?

    with open(filename, "r") as book:
        for line in book:
            words = line.split()
            for word in words:
                word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if word not in freq:
                    freq[word] = 1
                else:
                    freq[word] += 1
         

    return freq



def main():
    print(word_frequencies("src/alice.txt"))

if __name__ == "__main__":
    main()
