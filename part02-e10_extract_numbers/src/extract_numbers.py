#!/usr/bin/env python3
'''
dont think i ever did nested try-except structures before, but it felt natural.
'''
def extract_numbers(s):
    numbers_maybe = s.split()
    numbers_yes = []
    for potentially_number in numbers_maybe:
        try:
            number = int(potentially_number)
            numbers_yes.append(number)
        except ValueError:
            try:
                number = float(potentially_number)
                numbers_yes.append(number)
            except ValueError:
                continue
    return numbers_yes

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
