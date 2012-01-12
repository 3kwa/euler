def distinct_a_to_b(maximum):
    """
    >>> len( distinct_a_to_b(5) )
    15
    """
    return set(a ** b for a in range(2, maximum + 1) for b in range(2, maximum + 1))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print len( distinct_a_to_b(100) )
