"""
brute force 7295372 19m
smart runs in 15s
"""

from fractions import Fraction, gcd

def brute(D):
    """
    >>> brute(8)
    3
    """
    result = set()
    lower = Fraction(1, 3)
    upper = Fraction(1, 2)
    for d in range(2, D + 1):
        for n in range(1, d + 1):
            man = Fraction(n, d)
            if lower < man < upper:
                result.add(man)
    return len(result)

def smart(D):
    """
    >>> smart(8)
    3
    """
    count = 0
    for d in range(3, D+1):
        start = int( 1. / 3 * d) + 1
        stop = int(1. / 2 * d) + 1
        for n in range(start, stop):
            if gcd(d, n) == 1:
                count += 1
    return count

import doctest
doctest.testmod()
print smart(12000)
