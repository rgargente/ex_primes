import math


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
    primes = []
    i = 0
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes


def get_primes_sieve(n):
    """
    This is a basic implementation of the sieve of Eratosthenes as explained here:
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    :param n: maximum generated number
    :return: a list of primes
    """
    assert n > 1

    a = [True] * (n - 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        j = i ** 2
        while j <= n:
            a[j - 2] = False
            j += i
    return [i + 2 for i, prime in enumerate(a) if prime and i + 2 <= n]


def get_primes_up_to_nth(n):
    # TODO Only for big n
    limit = n * (math.log(n) + math.log(math.log(n)) - 1)  # From the Prime Number Theorem
    limit = math.ceil(limit * 1.10)  # better be sure
    primes = get_primes_sieve(limit)
    while len(primes) < n:
        limit *= 1.2
        primes = get_primes_sieve(int(limit))
    return primes[0:n]
