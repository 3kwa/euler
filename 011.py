from operator import mul

fixture = """
1 2 3
4 5 6
7 8 9
"""

class Matrix(object):
    """
    >>> m = Matrix(fixture)
    """
    def __init__(self, source):
        self.grid = [[int(i) for i in l.split(' ')] for l in source.split('\n')[1:-1]]
    def row(self, index):
        """
        >>> m = Matrix(fixture)
        >>> m.row(0)
        [1, 2, 3]
        """
        return self.grid[index]
    def column(self, index):
        """
        >>> m = Matrix(fixture)
        >>> m.column(0)
        [1, 4, 7]
        """
        return [row[index] for row in self.grid]
    def cell(self, row, column):
        """
        >>> m = Matrix(fixture)
        >>> m.cell(1, 1)
        5
        """
        return self.grid[row][column]
    def diagonal(self, index):
        """
        >>> m = Matrix(fixture)
        >>> m.diagonal(0)
        [1, 5, 9]
        >>> m.diagonal(1)
        [2, 6]
        >>> m.diagonal(-1)
        [4, 8]
        """
        delta = abs(index)
        range_ = range(len(self.grid) - delta)
        if index >= 0:
            return [self.cell(i, i + delta) for i in range_]
        else:
            return [self.cell(i + delta, i) for i in range_]
    def traversal(self, index):
        """
        >>> m = Matrix(fixture)
        >>> m.traversal(0)
        [7, 5, 3]
        >>> m.traversal(1)
        [8, 6]
        >>> m.traversal(2)
        [9]
        >>> m.traversal(-1)
        [4, 2]
        >>> m.traversal(-2)
        [1]
        """
        delta = abs(index)
        range_ = range(len(self.grid) - delta)
        if index >= 0:
            return [self.cell(len(self.grid) - i - 1, i + delta) for i in range_]
        else:
            return [self.cell(len(self.grid) - i - 1 - delta, i) for i in range_]


def product_of_n(matrix, n=4):
    """
    >>> m = Matrix(fixture)
    >>> p = product_of_n(m, 2)
    >>> p.next()
    4
    >>> p.next()
    28
    >>> p.next()
    10
    >>> list(p)
    [40, 18, 54, 2, 6, 20, 30, 56, 72, 32, 5, 45, 12, 8, 35, 15, 48]
    """
    # column
    for i in range(len(matrix.grid)):
        column = matrix.column(i)
        if len(column) >= n:
            for j in range(len(column) - n + 1):
                yield reduce(mul, column[j:j+n])
    # row
    for i in range(len(matrix.grid)):
        row = matrix.row(i)
        if len(row) >= n:
            for j in range(len(row) - n + 1):
                yield reduce(mul, row[j:j+n])
    # diagonal
    for i in range(-len(matrix.grid) + 1, len(matrix.grid)):
        diag = matrix.diagonal(i)
        if len(diag) >= n:
            for j in range(len(diag) - n + 1):
                yield reduce(mul, diag[j:j+n])
    # traversal
    for i in range(-len(matrix.grid) + 1, len(matrix.grid)):
        trav = matrix.traversal(i)
        if len(trav) >= n:
            for j in range(len(trav) - n + 1):
                yield reduce(mul, trav[j:j+n])



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)

    source = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
    """

    m = Matrix(source)
    print max(p for p in product_of_n(m, 4))
