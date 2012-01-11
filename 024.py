from itertools import permutations

def lexicographic_permutation(elements):
    """
    >>> lp = lexicographic_permutation('012')

    ['012', '021', '102', '120', '201', '210']
    """
    # the Python standard library way (fastest)
    #for value in permutations(elements):
        #yield ''.join(value)

    # the "ugly" I am experiementing way
    #source = list(elements)
    #selected = list()
    #for i in source:
        #selected.append(i)
        #for j in (c for c in source if c not in selected):
            #selected.append(j)
            #for k in (c for c in source if c not in selected):
                #selected.append(k)
                #yield ''.join( selected )
                #selected.remove(k)
            #selected.remove(j)
        #selected.remove(i)

    # SEPA algorithm http://www.freewebz.com/permute/soda_submit.html
    permutation = elements
    while permutation is not None:
        yield permutation
        permutation = sepa(permutation)

def find_key(permutation):
    """
    >>> find_key('012')
    ('0', '1', '2')
    >>> find_key('021')
    ('', '0', '21')
    >>> find_key('210')
    """
    for i in range(len(permutation) -1, 0, -1):
        if permutation[i-1] < permutation[i]:
            # head, key, tail
            return permutation[:i-1], permutation[i-1], permutation[i:]

def find_smallest_bigger_and_swap(key, tail):
    """
    >>> find_smallest_bigger_and_swap('1', '2')
    ('2', '1')
    """
    tail = list(tail)[::-1]
    for index, element in enumerate(tail):
        if element > key:
            key, tail[index] = element, key
            # new key, new tail
            return key, ''.join(tail[::-1])

def sepa(permutation):
    """
    >>> sepa('012')
    '021'
    >>> sepa('021')
    '102'
    >>> sepa('210')
    """
    try:
        head, key, tail = find_key(permutation)
    except TypeError:
        return None
    key, tail = find_smallest_bigger_and_swap(key, tail)
    tail = ''.join(sorted(tail))
    return ''.join((head, key, tail))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    generator = lexicographic_permutation('0123456789')
    i=1
    while i <= 1000000:
        value = generator.next()
        i += 1
    print value

