import primes

print sum(p for p in primes.generator(2000000))
