def pascal_diagonal(item):
    """
    1
    1 2
    1 3 6
    1 4 10 20
    1 5 15 35 70
    ...

    >>> pascal_diagonal(0)
    1
    >>> pascal_diagonal(1)
    2
    >>> pascal_diagonal(2)
    6
    >>> pascal_diagonal(3)
    20
    >>> pascal_diagonal(4)
    70
    """
    line = [1]
    for i in range(item):
        prev_line = line
        line = [1]
        for index, value in enumerate(prev_line[1:]):
            line.append(value + line[index])
        line.append(line[-1] + sum(prev_line))
    return line[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)
    print pascal_diagonal(20)

