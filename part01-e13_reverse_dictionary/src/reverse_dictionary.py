#!/usr/bin/env python3
'''
ignoring the synonyms aspect initially. feels like fine course of action
and fixing it later seems fine.

and so it was, not difficult.

'''
def reverse_dictionary(d):
    new_dict = {}

    
    for key, value in d.items():
        for item in value:
            if item not in new_dict:
                new_dict[item] = [key]
            else:
                new_dict[item].append(key)

    return new_dict

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 
       'six': ['kuusi'], 'fir': ['kuusi']}
    rd = reverse_dictionary(d)
    print(rd)
if __name__ == "__main__":
    main()
