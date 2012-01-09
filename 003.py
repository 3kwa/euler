def primeGenerator():
    # http://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf
    # http://stackoverflow.com/questions/567222/simple-prime-generator-in-python
    D = {}
    q = 2
    while True:
        if q not in D:
            D[q * q] = [q]
            yield q
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def decompose(number):
    prime = primeGenerator()
    for p in prime:
        if number < p / 2:
            break
        if number % p == 0:
            number = multiple_div(number, p)
            yield p

def multiple_div(number, div):
    # not necessary but more accurate
    if number % div == 0:
        return multiple_div(number / div, div)
    else:
        return number

if __name__ == '__main__':
    print max(p for p in decompose(600851475143))
