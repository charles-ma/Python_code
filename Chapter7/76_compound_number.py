import types

class Complex_number(object):
    '''Defines a complex number and some of the usual arithmetics.'''
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other_complex):
        sum_real = self.real + other_complex.real
        sum_imaginary = self.imaginary + other_complex.imaginary
        return Complex_number(sum_real, sum_imaginary)

    def __sub__(self, other_complex):
        sub_real = self.real - other_complex.real
        sub_imaginary = self.imaginary - other_complex.imaginary
        return Complex_number(sub_real, sub_imaginary)

    def __mul__(self, other_complex):
        mul_real = self.real * other_complex.real - self.imaginary * other_complex.imaginary
        mul_imaginary = self.real * other_complex.imaginary + self.imaginary * other_complex.real
        return Complex_number(mul_real, mul_imaginary)

    def __str__(self):
        if self.imaginary < 0:
            return str(self.real) + str(self.imaginary) + 'I'
        return str(self.real) + '+' + str(self.imaginary) + 'I'

c = Complex_number(2,5.5)
d = Complex_number(6, -1)
print c, d
print c + d
print c - d
print c * d
