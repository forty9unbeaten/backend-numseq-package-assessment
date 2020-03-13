def primes(n):
    '''Returns a list of all prime numbers less than n'''
    pass


def is_prime(m):
    '''Returns a boolean indicating whether m is a prime number'''
    if m > 1:
        for i in range(2, m):
            if m % i == 0:
                return False
        return True
    return False
