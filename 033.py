"""
49 / 98 == 4 / 8 in real math and also by crazy 9 (nine) simplification

there are only 4 such fractions less than 1 with double digit numerator and
denominator (ignoring the trivial 0 cases)
"""

def cancel(a, b):
    """
    2 double digit parameters returnt the "simplified" division

    >>> cancel(49, 98)
    0.5
    """
    a, b = list(str(a)), list(str(b))
    for d in a:
        if d in b:
            a.remove(d)
            b.remove(d)
    if len(a) == 1:
        try:
            return int(''.join(a)) / float(''.join(b))
        except ZeroDivisionError:
            pass

def trivial(a, b):
    """
    >>> trivial(49, 98)
    False
    >>> trivial(30, 50)
    True
    """
    if a % 10 and b % 10:
        return False
    return True

if __name__=='__main__':
    import doctest
    doctest.testmod()

    only_four = []
    for i in range(11,100):
        for j in range(11,100):
            div = i / float(j)
            if div == cancel(i,j) and div < 1 and not trivial(i, j):
                only_four.append((i, j))

    print only_four
    print reduce(lambda x, y : (x[0] * y[0], x[1] * y[1]), only_four)


