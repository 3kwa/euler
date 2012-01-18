"""
Truncatable prime from left to right and right to left implies it has to
start and finsh with 2, 3, 5 or 7

Using the fact that only eleven primes can be both.
"""

from primes import generator, is_prime

def truncate(number):
    """
    >>> truncate(3797)
    [797, 3, 97, 37, 7, 379]
    """
    string = str(number)
    result = []
    for i in range(1, len(string)):
        result.append(int(string[i:]))
        result.append(int(string[:i]))
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    g = generator()
    truncatables_primes = []
    while len(truncatables_primes) < 11:
        prime = g.next()
        if prime in (2, 3, 5, 7):
            continue
        if all(map(is_prime, truncate(prime))):
            truncatables_primes.append(prime)
    print truncatables_primes
    print sum(truncatables_primes)
