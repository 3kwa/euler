"""
A naive implementation (code first approach :P) makes us notice that the
numerator is always very close to 3 * D / 7

Hence an effective approach is to start from d = D and decrease ...
"""

from fractions import Fraction

def naive(D):
    """
    >>> naive(10)
    Fraction(2, 5)
    """
    left = 0
    ref = Fraction(3, 7)
    for d in range(1, D + 1):
        for n in range(1, d * 3 / 7 + 1):
            if left < Fraction(n, d) < ref:
                left = Fraction(n, d)
    return left

def effective(D):
    """
    >>> effective(10)
    Fraction(2, 5)
    >>> effective(100)
    Fraction(41, 96)
    >>> effective(1000)
    Fraction(428, 999)
    >>> effective(10000)
    Fraction(4283, 9994)
    """
    candidates = list(Fraction(3 * d / 7, d) for d in range(D, D - 50, -1) if d > 0)
    return max(candidate for candidate in candidates if candidate < Fraction(3, 7))


import doctest
doctest.testmod()

print effective(1000000)
