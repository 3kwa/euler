"""
Initially was hoping on doing sum(1 for i in range(1,1000) if test(fraction(i)))
but was too slow so moved the test in the generation and returned a tuple instead
"""

from fractions import Fraction

def fraction(n):
    """
    >>> fraction(1)
    (0, Fraction(3, 2))
    >>> fraction(2)
    (0, Fraction(7, 5))
    >>> fraction(8)
    (1, Fraction(1393, 985))
    """
    count = 0
    result = Fraction(2, 1)
    for i in range(1, n):
        result = 2 + Fraction(1, result)
        if test(1 +Fraction(1, result)):
            count += 1
    return count, 1 + Fraction(1, result)

def test(fraction):
    """
    >>> test(Fraction(7, 5))
    False
    >>> test(Fraction(1393, 985))
    True
    """
    return len(str(fraction.numerator)) > len(str(fraction.denominator))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print fraction(1000)[0]
