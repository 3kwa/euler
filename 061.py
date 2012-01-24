from itertools import permutations

def triangle(n):
    return n * (n + 1) / 2

def square(n):
    return n * n

def pentagonal(n):
    return n * (3 * n - 1) / 2

def hexagonal(n):
    return n * (2 * n - 1)

def heptagonal(n):
    return n * (5 * n - 3) / 2

def octagonal(n):
    return n * (3 * n - 2)

T = [t for t in (triangle(n) for n in range(1,4000)) if 1000<= t <= 9999]
S = [t for t in (square(n) for n in range(1,4000)) if 1000<= t <= 9999]
P = [t for t in (pentagonal(n) for n in range(1,4000)) if 1000<= t <= 9999]
Hx = [t for t in (hexagonal(n) for n in range(1,4000)) if 1000<= t <= 9999]
Hp = [t for t in (heptagonal(n) for n in range(1,4000)) if 1000<= t <= 9999]
O = [t for t in (octagonal(n) for n in range(1,4000)) if 1000<= t <= 9999]


def recursive(list_, acc=[]):
    if len(list_) == 0:
        if str(acc[0])[:2] == str(acc[-1])[-2:]:
            return acc
        return
    number = acc[-1]
    last_2 = str(number)[-2:]
    for other in list_[0]:
        first_2 = str(other)[:2]
        if first_2 == last_2:
            return recursive(list_[1:], acc + [other])


permutation = permutations([T, S, P, Hx, Hp, O])
result = None
while result is None:
    p = permutation.next()
    for n in p[0]:
        result = recursive(p[1:], [n])
        if result is not None:
            break
print result, sum(result)
