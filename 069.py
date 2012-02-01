"""
Not the fastest but returns the correct answer using my brain instead of jumping
into coding could have been good :D

prime factorisation of n, n = P_i ( pi ** ei )
phi(n) = n * P_i ( 1 - 1 / pi )
n / phi(n) = 1 / P_i ( 1 - 1 / pi )

We want max n / phi(n) hence we need a small denominator P_i ( 1 - 1 / pi )
which is obtain for small values of pi

2 * 3 = 6
2 * 3 * 5 = 30
2 * 3 * 5 * 7 = 210
2 * 3 * 5 * 7 * 11  = 2310
2 * 3 * 5 * 7 * 11 * 13 = 30030
2 * 3 * 5 * 7 * 11 * 13 * 17 = ...

Smallest n under 1 000 000 giving a a max n / phi(n)
"""

from operator import mul
from primes import generator

primes = list( generator(1000000) )
set_ = set( primes )

def factors(number):
    """
    >>> f = factors(4)
    >>> f.next()
    (2, 2)
    >>> list(factors(6))
    [(2, 1), (3, 1)]
    >>> list(factors(12))
    [(2, 2), (3, 1)]
    """
    for p in primes:
        if number < p / 2:
            break
        if number % p == 0:
            e = exponent(number, p)
            number = number / (p ** e)
            yield p, e

def exponent(number, prime):
    """
    >>> exponent(2, 2)
    1
    >>> exponent(8, 2)
    3
    >>> exponent(12, 2)
    2
    """
    e = 0
    while number % prime == 0:
        e += 1
        number = number / prime
    return e

def totient(n):
    """
    >>> totient(9)
    6
    >>> totient(36)
    12
    """
    if n in set_:
        return n - 1
    return int( n * reduce(mul, ((1 - 1. / p) for p, e in factors(n))) )

import doctest
doctest.testmod()

n_max = 0
max_ = 0
i = 2
N = 1000000
while i < N:
    man = float(i) / totient(i)
    n_max, max_ = (i, man) if man > max_ else (n_max, max_)
    i += 1

print n_max, max_
