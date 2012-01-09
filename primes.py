def generator(stop=None):
    """
    http://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf
    http://stackoverflow.com/questions/567222/simple-prime-generator-in-python

    >>> list(generator(2))
    [2]
    >>> p = generator()
    >>> p.next()
    2
    >>> p.next()
    3
    """
    D = {}
    q = 2
    while (q <= stop if stop is not None else True):
        if q not in D:
            D[q * q] = [q]
            yield q
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)
