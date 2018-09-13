import pytest

import primes


@pytest.fixture()
def primelist():
    with open('primelist.txt') as f:
        read_data = f.read()
    return list(map(int, read_data.split()))


def test_isprime(primelist):
    for n in range(1000):
        assert (primes.is_prime(n)) == (n in primelist)

def test_n_lessthan_1():
    with pytest.raises(AssertionError):
        primes.get_primes_sieve(1)
    with pytest.raises(AssertionError):
        primes.get_primes_sieve(0)
    with pytest.raises(AssertionError):
        primes.get_primes_sieve(-1)


@pytest.mark.parametrize("max, n", [  # maximum prime value and number of primes in the result
    (30, 10),
    (71, 20),
])
def test_get_primes_sieve(max, n):
    expected = primelist()[0:n]
    assert expected == primes.get_primes_sieve(max)


@pytest.mark.parametrize("n, function", [
    (10, primes.get_primes_up_to_nth_simple),
    (10, primes.get_primes_up_to_nth),
    (1000, primes.get_primes_up_to_nth_simple),
    (1000, primes.get_primes_up_to_nth),
    (10000, primes.get_primes_up_to_nth_simple),
    (10000, primes.get_primes_up_to_nth)
])
def test_get_primes_up_to_nth(primelist, n, function):
    assert primelist[0:n] == function(n)
