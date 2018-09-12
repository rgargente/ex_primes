import math


def get_primes(n):
    """
    This is a basic implementation of the sieve of Eratosthenes as explained here:
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    :param n: maximum generated number
    :return: a list of primes
    """
    assert n > 1

    a = [True] * (n-1)
    for i in range(2, int(math.sqrt(n))+1):
        j = i**2
        while j <= n:
            a[j-2] = False
            j += i
    return [i+2 for i,prime in enumerate(a) if prime and i +2<= n]
