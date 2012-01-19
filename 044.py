def P(n):
    return n * (3 * n - 1) / 2

max_ = 2170 # set at 5000 first run and reduced later

pentagonals = {P(1)}
for n in range(2, 2 * max_):
    pentagonals.add(P(n))

D = None
for j in range(1, max_):
    for k in range(j, max_):
        if P(k) - P(j) in pentagonals  and P(k) + P(j) in pentagonals:
            D = P(k) - P(j)
            break
    if D is not None:
        break
print D
