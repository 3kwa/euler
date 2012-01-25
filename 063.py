"""
a ** b

if a >= 10 a ** b for b > 2 will always have at least one more digit than
the value b

a in [1,9]

was lucky with the upper bound on my first try but ...

x ** n has n digits when 10 ** (n - 1) <= x ** n < 10 * n

10 ** (n - 1) = x ** n
0.1  * 10 ** n = x ** n
log(0.1) + n * log(10) = n * log(x)
n * (log(10) - log(x)) = log(10)
n = log(10) / (log(10) - log(x))

for x = 9 gives n = 22
"""

print sum(1 for a in range(1,10) for b in range(1,22) if len(str(a ** b)) == b)
