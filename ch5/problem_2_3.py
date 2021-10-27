from numbers import Rational
import math
from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError
        common_divisor = gcd(numerator, denominator)
        numerator = numerator / common_divisor
        denominator = denominator / common_divisor
        if denominator < 0:
            numerator = numerator * -1
            denominator = denominator * -1
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def __add__(self, other):
        if isinstance(other, int):
            numerator = self.numerator + other * self.denominator
            return Fraction(numerator, self.denominator)
        else:
            if isinstance(other, float):
                other = Fraction.transfer_from_float(other)
            numerator = self.numerator * other.denominator + other.numerator * self.denominator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, int):
            numerator = self.numerator - other * self.denominator
            return Fraction(numerator, self.denominator)
        else:
            if isinstance(other, float):
                other = Fraction.transfer_from_float(other)
            numerator = self.numerator * other.denominator - other.numerator * self.denominator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)

    def __rsub__(self, other):
        return -Fraction.__sub__(self, other)

    def __mul__(self, other):
        if isinstance(other, int):
            return Fraction(self.numerator * other, self.denominator)
        else:
            if isinstance(other, float):
                other = Fraction.transfer_from_float(other)
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, int):
            return Fraction(self.numerator, self.denominator * other)
        else:
            if isinstance(other, float):
                other = Fraction.transfer_from_float(other)
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Fraction(numerator, denominator)

    def __rtruediv__(self, other):
        numerator = Fraction.__truediv__(self,other).denominator
        denominator = Fraction.__truediv__(self,other).numerator
        return Fraction(numerator,denominator)

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __repr__(self):
        return f'Fraction({self.numerator}, {self.denominator})'

    def __eq__(self, other):
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        else:
            return False
    @staticmethod
    def transfer_from_float(f):
        p = len(str(f).split('.')[1])
        other_numerator = math.ceil(f * pow(10, p))
        other_denominator = pow(10, p)
        other = Fraction(other_numerator, other_denominator)
        return other

# print(Fraction(1,2)+0.4)
# print(Fraction(1,2)-0.2)
# print(Fraction(3, 4) - 0.125)
# print(Fraction(4, 5) / 0.4)
# print(0.8 / Fraction(3, 1))
# print(3 * Fraction(4, 3))
# x = 0.0999
# print(str(x))
# print(str(x).split("."))
# print(len(str(x).split(".")[1]))
# print(pow(10, len(str(x).split('.')[1])))
# print(0.0006 * 10000)
# print(x * pow(10, len(str(x).split('.')[1])))
# print(math.ceil(x * pow(10, len(str(x).split('.')[1]))))
# 30min