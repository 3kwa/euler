from fractions import Fraction

D = 12000
result = set()
lower = Fraction(1, 3)
upper = Fraction(1, 2)
for d in range(2, D + 1):
    for n in range(1, d + 1):
        man = Fraction(n, d)
        if lower < man < upper:
            result.add(man)
print len(result)
