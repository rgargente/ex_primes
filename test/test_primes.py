import pytest

import primes


@pytest.fixture()
def primelist():
    with open('primelist.txt') as f:
        read_data = f.read()
    return list(map(int, read_data.split()))


def test_n_lessthan_1():
    with pytest.raises(AssertionError):
        primes.get_primes(1)
    with pytest.raises(AssertionError):
        primes.get_primes(0)
    with pytest.raises(AssertionError):
        primes.get_primes(-1)


PRIMES30 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
PRIMES71 = PRIMES30 + [31, 37, 41, 43, 47, 53, 59, 61, 67, 71]


@pytest.mark.parametrize("max, n", [  # maximum prime value and number of primes in the result
    (30, 10),
    (71, 20),
])
def test_getprimes(max, n):
    expected = primelist()[0:n]
    assert expected == primes.get_primes(max)


@pytest.mark.parametrize("n", [10, 1000, 10000])
def test_get_primes_up_to_nth(primelist, n):
    assert primelist[0:n] == primes.get_primes_up_to_nth(n)
