from tabulate import tabulate
import primes
import numpy as np

if __name__ == "__main__":
    primes10 = primes.get_primes(10)
    size = len(primes10)
    rows = np.tile(primes10, (size, 1))
    for i, p in enumerate(primes10):
        rows[i, :] *= p
    rows = np.c_[primes10, rows]
    print(tabulate(rows, headers=[''] + primes10, tablefmt='grid'))
