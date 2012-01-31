"""
http://mathworld.wolfram.com/PellEquation.html
"""

from math import sqrt
from itertools import cycle


def continued_fraction(N):
    """
    >>> gen = continued_fraction(23)
    >>> [gen.next() for i in range(5)]
    [4, 1, 3, 1, 8]
    """
    a = a0 = int(sqrt(N))
    d = 1
    m = 0
    seen = set((a, d, m))
    while True:
        yield a
        m_ = a*d - m
        d_ = (N - m_ ** 2) / d
        a_ = (a0 + m_) / d_
        a, d, m = a_, d_, m_
        if (a_, d_, m_) in seen:
            return
        seen.add( (a, d, m) )

def convergents(N, n):
    """
    >>> convergents(2, 1)
    (3, 2)
    >>> convergents(2, 2)
    (7, 5)
    """
    a = list( continued_fraction(N) )
    p_ = a[0]
    p = a[0]*a[1] + 1
    q_ = 1
    q = a[1]
    if n == 1:
        return p, q
    gen = cycle(a[1:])
    gen.next()
    for i in range(1,n):
        a_ = gen.next()
        p_, p = p, a_ * p + p_
        q_, q = q, a_ * q + q_
    return p, q

def solve(D):
    """
    >>> solve(13)
    (649, 180)
    >>> [solve(i) for i in (2, 3, 5, 6, 7)]
    [(3, 2), (2, 1), (9, 4), (5, 2), (8, 3)]

    putting it all together

    >>> solution, D = max((solve(i), i) for i in range(8) if int(sqrt(i)) != sqrt(i) )
    >>> solution
    (9, 4)
    >>> D
    5
    """
    r = len( list(continued_fraction(D))[1:] )
    if r % 2 == 0:
        return convergents(D, r - 1)
    else:
        return convergents(D, 2 * r - 1)

import doctest
doctest.testmod()
solution, D = max((solve(i), i) for i in range(1001) if int(sqrt(i)) != sqrt(i) )
print D
