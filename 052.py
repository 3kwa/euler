def process(n):
    """
    Return the smallest integer which has the same digits when multiplied n times

    >>> process(2)
    125874
    """
    if n < 2:
        return
    i = 1
    while True:
        ref = set(str(i))
        if any(ref != set(str(i * m)) for m in range(2, n + 1)):
            i += 1
        elif any(len(ref) != len(str(i * m)) for m in range(2, n + 1)):
            i += 1
        else:
            return i

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print process(6)
