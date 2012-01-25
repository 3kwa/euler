from math import sqrt


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

def period(N):
    """
    >>> [period(n) for n in (2, 3, 5, 6, 7, 8, 10, 11, 12, 13)]
    [1, 2, 1, 2, 4, 2, 1, 2, 2, 5]
    >>> period(23)
    4
    """
    value = sqrt(N)
    if int(value)==value:
        return 0
    return len(list(continued_fraction(N))) - 1

def solution(max):
    """
    >>> solution(13)
    4
    """
    return sum(1 for n in range(2, max + 1) if period(n) % 2 != 0)


import doctest
doctest.testmod()

print solution(10000)
