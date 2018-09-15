import math

import numpy as np


def is_prime(n):
    """
    As explained in:
    https://en.wikipedia.org/wiki/Primality_test
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


def get_primes_up_to_nth_simple(n):
    primes = np.empty(n)
    i = 0
    i_prime = 0
    while i_prime < n:
        if is_prime(i):
            primes[i_prime] = i
            i_prime += 1
        i += 1
    return primes.astype(int).tolist()


def get_primes_sieve(n):
    """
    This is a basic implementation of the sieve of Eratosthenes as explained here:
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    :param n: maximum generated number
    :return: a list of primes
    """
    assert n > 1

    a = np.full(n - 1, True)
    for i in range(2, int(math.sqrt(n)) + 1):
        j = i ** 2
        while j <= n:
            a[j - 2] = False
            j += i
    return [i + 2 for i, prime in enumerate(a.astype(int)) if prime and i + 2 <= n]


def get_primes_up_to_nth_sieve(n):
    limit = n * (math.log(n) + math.log(math.log(n)) - 1)  # From the Prime Number Theorem
    limit = math.ceil(limit * 1.10)  # better be sure
    primes = get_primes_sieve(limit)
    while len(primes) < n:
        limit *= 1.2
        primes = get_primes_sieve(int(limit))
    return primes[0:n]


def get_primes_up_to_nth_smart(n):
    if n < 100:
        return get_primes_up_to_nth_simple(n)
    else:
        return get_primes_up_to_nth_sieve(n)
