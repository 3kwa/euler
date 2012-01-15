"""
Exploration first ... and elegant recursive solution later ;)

from operator import mul

REF = [1, 2, 5, 10, 20, 50, 100, 200]
TARGET = target = 200

# The combinatorial explosion ...

for target in (1, 2, 5, 10, 20, 50, 100, 200):
    print reduce(mul, (target / coin + 1 for coin in REF))

def evaluate(count, value):
    return sum(n * value[index] for index, n in enumerate(count))

total = 0
loops = 0
t1 = 200
for i in range(t1/1+1):
    # reducing the combinatorial factor every iteration ...
    t2 = t1 - i * 1
    for j in range(t2/2+1):
        t3 = t2 - j * 2
        for k in range(t3/5+1):
            t4 = t3 - k * 5
            for l in range(t4/10+1):
                t5 = t4 - l * 10
                for m in range(t5/20+1):
                    t6 = t5 - m * 20
                    for n in range(t6/50+1):
                        t7 = t6 - 50 * n
                        for o in range(t7/100+1):
                            t8 = t7 - o * 100
                            for p in range(t8/200+1):
                                if evaluate([i,j, k, l, m, n, o, p], REF) == target:
                                    total += 1
                                loops += 1
print total
print loops
"""

class Singleton(object):
    """
    Using a Singleton beats using a global in the recursion, if for no other
    reason than : tricky to declare a global in a doctest :D
    """
    value = 0

def recursion_singleton(coins, target, count):
    """
    >>> count = Singleton()
    >>> recursion_singleton([1, 2, 5, 10, 20, 50, 100, 200], 20, count)
    >>> print count.value
    41
    """
    if target == 0:
        count.value += 1
        return
    if len(coins) == 0:
        return
    for n in range(target/coins[0] + 1):
        recursion_singleton(coins[1:], target - n * coins[0], count)


def recursion_genexp(coins, target):
    """
    Maybe more elegant but two (2) times slower than the recursion with singleton

    >>> recursion_genexp([1, 2, 5, 10, 20, 50, 100, 200], 20)
    41
    """
    if target == 0:
        return 1
    if len(coins) == 0:
        return 0
    return sum(recursion_genexp(coins[1:], target - n * coins[0]) for n in range(target/coins[0] + 1))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    count = Singleton()
    recursion_singleton([1, 2, 5, 10, 20, 50, 100, 200], 200, count)
    print count.value
