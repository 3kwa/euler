def length_cycle_for_unit_fraction(n):
    """
    >>> length_cycle_for_unit_fraction(7)
    6
    >>> length_cycle_for_unit_fraction(6)
    1
    >>> length_cycle_for_unit_fraction(2)
    0
    """

    # when the remainder has already been hit the decimal cycle (re)starts
    # http://en.wikipedia.org/wiki/Repeating_decimal

    remainder = []

    r = 1 % n
    num = r * 10
    while r not in remainder:
        remainder.append(r)
        r = num % n
        num = r * 10

    # if r = 0 we have a terminating decimal
    return len(remainder) - remainder.index(r) if r else r

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print max(
            ( d for d in range(1,1000) ),
            key = lambda d: length_cycle_for_unit_fraction(d)
            )
