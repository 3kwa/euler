def triangles():
    """
    >>> generator = triangles()
    >>> [generator.next() for i in range(10)]
    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    """
    n = 1
    while True:
        yield n * (n + 1) / 2
        n += 1
def convert(word):
    """
    >>> convert('SKY')
    55
    """
    return sum(ord(c) - ord('A') + 1 for c in word)



if __name__ == '__main__':
    import doctest
    doctest.testmod()

    with open('words.txt') as f:
        words = f.read().replace('"','').split(',')

    max_ = max(convert(word) for word in words)

    generator  = triangles()
    value = generator.next()
    hash_ = {value}
    while value <= max_:
        hash_.add(value)
        value = generator.next()

    print sum(1 for word in words if convert(word) in hash_)
