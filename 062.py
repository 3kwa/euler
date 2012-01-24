"""
For 3 permuation a "naive" method works but for higher orders a combinatorial
explosion is certain 10! permutation to explore for a 10 digits cube.

increment i
calculate i's cube
order the digit of the cube (shared by all permutations)
store the cube in a list in a dict which key is the order
when the length of the list of cuve for a key reaches permutation we are done!
"""

from collections import defaultdict

def find(permutation):
    """
    >>> find(3)
    41063625
    """
    seen = defaultdict(list)
    i = 1
    while True:
        cube = i ** 3
        key = ''.join( sorted(digit for digit in str(cube)) )
        seen[key].append(cube)
        if len(seen[key]) == permutation:
            return min(seen[key])
        i += 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print find(5)
