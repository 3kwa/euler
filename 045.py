"""
all hexagonal numbers are also triangle numbers

the intersection of 2 sets A and B is A - (A - B)
"""

def P(n):
    return n * (3 * n - 1) / 2

def H(n):
    return n * (2 * n - 1)

max_ = 100000

pentagonals = {P(n) for n in range(1, max_)}
hexagonals = {H(n) for n in range(1, max_)}

print pentagonals - (pentagonals - hexagonals)
