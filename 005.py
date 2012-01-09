from operator import mul

def evenly_divisible(number, range_):
    """
    >>> evenly_divisible(2520, range(1,11))
    True
    """
    return all(number % p == 0 for p in range_)

def smallest_evenly_divisible(range_):
    """
    >>> smallest_evenly_divisible(range(1, 11))
    2520
    """
    for i in xrange(1, reduce(mul, range_)+1):
        if evenly_divisible(i, range_):
            return i

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)
    print smallest_evenly_divisible(range(1, 21))
