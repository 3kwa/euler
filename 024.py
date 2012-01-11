from itertools import permutations

def lexicographic_permutation(elements):
    """
    >>> lp = lexicographic_permutation('012')
    >>> list(lp)
    ['012', '021', '102', '120', '201', '210']
    """
    for value in permutations(elements):
        yield ''.join(value)
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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    generator = lexicographic_permutation('0123456789')
    i=1
    while i <= 1000000:
        value = generator.next()
        i += 1
    print value

