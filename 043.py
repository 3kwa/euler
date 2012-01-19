from operator import mul

def recursive(selected=[]):
    """
    recursive generator of 0 to 9 pandigital numbers

    >>> generator = recursive()
    >>> [generator.next() for i in range(5)]
    [123456789, 123456798, 123456879, 123456897, 123456978]
    """
    if len(selected) == 10:
        yield int( ''.join(map(str, selected)) )
    for i in range(10):
        if i not in selected:
            for result in recursive(selected + [i]):
                yield result

def condition(number):
    """
    >>> condition(1406357289)
    True
    >>> condition(1406537289)
    False
    """
    string = str(number)
    return not any([
        int(string[1:4]) % 2,
        int(string[2:5]) % 3,
        int(string[3:6]) % 5,
        int(string[4:7]) % 7,
        int(string[5:8]) % 11,
        int(string[6:9]) % 13,
        int(string[7:10]) % 17
        ])


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print sum(number for number in recursive() if condition(number))
