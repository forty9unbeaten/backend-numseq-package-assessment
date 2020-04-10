def square(n):
    '''Returns the nth term of the numbers that can be
     arranged as symmetric cube shapes'''
    return n ** 2


def triangle(n):
    '''Returns the nth term of the numbers that can be
     arranged in triangular geometric shapes'''
    if n > 0:
        return sum([i for i in range(1, n + 1)])
    return 0


def cube(n):
    '''Returns the nth term of the numbers that can be
     arranged as symmetric cube shapes'''
    return n ** 3
