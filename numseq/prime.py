def primes(n):
    '''Returns a list of all prime numbers less than n'''
    # ALOT of reading to understand Sieve of Eratosthenes algorithm...WOW

    if n > 2:
        prime_nums = [True] * n
        multiplier = 2
        stopper = int(n ** .5)
        while multiplier <= stopper:
            if prime_nums[multiplier]:
                for i in range(multiplier * multiplier, n, multiplier):
                    if prime_nums[i]:
                        prime_nums[i] = False
            multiplier += 1
        return [i for i in range(2, n) if prime_nums[i]]
    else:
        return []


def is_prime(m):
    '''Returns a boolean indicating whether m is a prime number'''
    if m > 1:
        for i in range(2, m):
            if m % i == 0:
                return False
        return True
    return False
