#!/usr/bin/env python3
'''
simple enough, but good recitement(yeah, thats not the word i was looking for but close enough)
'''
class Rational(object):

    def __init__(self, numerator : int, denominator : int):

        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    #operations + - * / < > == (no reducing the fraction required)
    def __add__(self, other):
        newden = self.denominator * other.denominator
        newnum = self.numerator * other.denominator + other.numerator * self.denominator
        return Rational(newnum, newden)

    def __sub__(self, other):
        newden = self.denominator * other.denominator
        newnum = self.numerator * other.denominator - other.numerator * self.denominator
        return Rational(newnum, newden)

    def __mul__(self, other):
        newnum = self.numerator * other.numerator
        newdem = self.denominator * other.denominator

        #product = Rational(newnum, newdem)
        return Rational(newnum, newdem)#product

    def __truediv__(self, other):
        newnum = self.numerator * other.denominator
        newden = self.denominator * other.numerator
        
        quotient = Rational(newnum, newden)
        return quotient

    def __lt__(self, other):
        if self.numerator / self.denominator < other.numerator / other.denominator:
            return True
        return False

    def __gt__(self, other):
        if self.numerator / self.denominator > other.numerator / other.denominator:
            return True
        return False
    def __eq__(self, other):
        if self.numerator / self.denominator == other.numerator / other.denominator:
            return True
        return False

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
