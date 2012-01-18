"""
Should explore the potential of a generator base approach using
http://mathworld.wolfram.com/PythagoreanTriple.html
"""

from math import sqrt

def solutions(perimeter):
    """
    >>> list(solutions(120))
    [(20, 48, 52), (24, 45, 51), (30, 40, 50)]
    """
    for a in range(1, perimeter / 2):
        for b in range(a, perimeter - a):
            c = sqrt(a ** 2 + b ** 2)
            if a + b + c == perimeter:
                yield a, b, int(c)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print max(
        ( (p, list(solutions(p))) for p in range(1, 1001) ),
        key= lambda x: len(x[1]) )
