def fibonacciGenerator(stop=4000000):
    prev, last = 1 , 0
    while last < stop:
        if last == 0:
            fib = 1
        else:
            fib = prev + last
        prev, last = last, fib
        yield fib

if  __name__ == '__main__':
    fib = fibonacciGenerator()
    print sum(i for i in fib if i % 2 == 0)
