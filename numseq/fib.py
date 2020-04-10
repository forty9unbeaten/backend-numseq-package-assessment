def fib(n):
    '''Return the nth number in the Fibonacci sequence'''
    a, b = 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for _ in range(1, n):
            a, b = b, a + b
        return b
