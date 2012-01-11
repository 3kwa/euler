def alphabetical_value(name):
    """
    >>> alphabetical_value('A')
    1
    >>> alphabetical_value('AB')
    3
    """
    return sum(ord(c) - 64 for c in name)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)

    with open('names.txt') as f:
        source = [name[1:-1] for name in f.read().split(',')]
    source.sort()

    print sum( (index + 1) * alphabetical_value(name) for index, name in enumerate(source))
