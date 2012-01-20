from primes import factors


def consecutive_distinct(count):
    """
    >>> consecutive_distinct(2)
    14
    >>> consecutive_distinct(3)
    644
    """
    result = None
    acc = set()
    consecutive = 1
    i = 1
    while result is None:
        i += 1
        new = set(factors(i))

        # does i have the correct number of factors
        if len(new) != count:
            consecutive = 1
            acc = set()
            continue

        # acc is empty and new is acceptable we are resetting
        if len(acc) == 0:
            consecutive = 1
            acc = new
            continue

        # are all of i's factor distinct from the previous 'count' i
        if len(acc.intersection(new)) != 0:
            consecutive = 1
            acc = new
            continue

        # increase the count of consecutive and add the factors to acc
        consecutive += 1
        acc = acc.union(new)

        if consecutive == count:
            result = i - count + 1

    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print consecutive_distinct(4)
