from operator import mul

REF = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200

for target in (1, 2, 5, 10, 20, 50, 100, 200):
    print reduce(mul, (target / coin + 1 for coin in REF))

def evaluate(count, value):
    return sum(n * value[index] for index, n in enumerate(count))

total = 0
loops = 0
t1 = 200
for i in range(t1/1+1):
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
