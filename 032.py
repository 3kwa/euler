def pandigitial_product(multiplicand, multiplier):
    """
    >>> pandigitial_product(39, 186)
    7254
    >>> pandigitial_product(1,3)
    0
    """
    product = multiplicand * multiplier
    string = ''.join( sorted(
        reduce( lambda x, y : str(x) + str(y),
        [product, multiplicand, multiplier]) ) )
    if string == '123456789':
        return product
    return 0

def t2i(tuple_):
    """
    >>> t2i((1, 2, 3))
    123
    """
    return int(''.join(map(str, tuple_)))

def brute(tuple_):
    """
    >>> brute((3, 9, 1, 8, 6, 7, 2, 5, 4))
    7254
    >>> brute((3, 9, 1, 8, 6, 7, 2, 4, 5))
    0
    """
    for i in range(1, len(tuple_) - 1):
        multiplicand = t2i(tuple_[:i])
        for j in range(i + 1, len(tuple_)):
            multiplier = t2i(tuple_[i:j])
            product = t2i(tuple_[j:])
            calculated = multiplicand * multiplier
            if calculated == product:
                return calculated
    return 0

def smart(list_):
    """
    A * B = C only 9 possible digits

    n(A) must be 1 or 2 with n(B) respecitively 4 or 3

    n(C) is 4

    >>> smart([3,9,1,8,6])
    7254
    """
    string = ''.join(map(str, list_))
    multiplicand = int(string[:2])
    multiplier = int(string[2:])
    return pandigitial_product(int(string[:1]), int(string[1:])) \
            + pandigitial_product(int(string[:2]), int(string[2:]))


def recursive(selected, size):
    """
    recursive generator used in the brute force approach to solving the problem
    """
    if len(selected) == size:
        yield selected
    for digit in range(1,10):
        if digit in selected:
            continue
        for result in recursive(selected + [digit], size):
            yield result


def generator():
    """
    smart and fast generator beats recursion anyday

    9 * 8 * 7 * 6 * 5 = 15120
    >>> len(list(generator()))
    15120
    """
    for i in range(1,10):
        for j in range(1,10):
            if j in [i]:
                continue
            for k in range(1,10):
                if k in [i,j]:
                    continue
                for l in range(1,10):
                    if l in [i,j,k]:
                        continue
                    for m in range(1,10):
                        if m in [i,j,k,l]:
                            continue
                        yield i, j, k, l, m


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print sum(set(smart(l) for l in generator()))
    print sum(set(brute(l) for l in recursive([], 9)))
