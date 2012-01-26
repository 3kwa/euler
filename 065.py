from fractions import Fraction

def continued_fraction():
    """
    >>> gen = continued_fraction()
    >>> [gen.next() for i in range(14)]
    [1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10]
    """
    k = 1
    while True:
        for i in (1, 2 * k, 1):
            yield i
        k += 1

def convergents(start, list_, n):
    """
    >>> convergents(1, (2, 2, 2, 2, 2, 2, 2, 2), 1)
    Fraction(3, 2)
    >>> convergents(1, (2, 2, 2, 2, 2, 2, 2, 2), 2)
    Fraction(7, 5)
    >>> convergents(1, (2, 2, 2, 2, 2, 2, 2, 2), 4)
    Fraction(41, 29)

    >>> gen = continued_fraction()
    >>> e = [gen.next() for i in range(10)]
    >>> [convergents(2, e, i) for i in range(1,10)]
    [Fraction(3, 1), Fraction(8, 3), Fraction(11, 4), Fraction(19, 7), Fraction(87, 32), Fraction(106, 39), Fraction(193, 71), Fraction(1264, 465), Fraction(1457, 536)]
    """
    man = list_[:n][::-1]
    result = Fraction(1, man[0])
    for d in man[1:]:
        result = Fraction(1, d + result)
    return start + result


import doctest
doctest.testmod()
gen = continued_fraction()
e = [gen.next() for i in range(100)]
print sum(int(d) for d in str(convergents(2, e, 99).numerator))
