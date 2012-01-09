import primes

p = primes.generator()
for i in range(10000):
    p.next()
print p.next()
