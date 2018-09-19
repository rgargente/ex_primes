# Prime generator exercise

This is a little program to generate a multiplication table of prime numbers, and an associated library to generate
prime numbers. It includes tests and benchmarks to compare different approaches.

## How to run the program

The zip file contains all the source code. It also contains a git bundle file in case you are interested in checking
the git history. There is more information about how to unbundle it here:
https://git-scm.com/docs/git-bundle

The exercise is implemented using Python 3. 

I have provided an Anaconda environment file to easily create an environment to run the software. If you have Anaconda
installed, simply run the following command in a terminal:
```
 conda env create -f environment.yml
```

Otherwise install each dependency using ```pip install ```. You can read the environment.yml file to know which 
dependencies you need, but I would recommend just installing whatever pyhton tells is missinge
since most of the dependencies should already be installed by default. 

## Design considerations

I have used a TDD approach to develop this solution. All the tests are inside the test folder.
There is also a benchmark to measure the speed of different algorithms. There is primes library and a primetable script.
The script uses the library to generate the prime numbers. 

I have implemented two different algorithms to generate primes. One just checks each odd number in sequence. The other 
uses the sieve of Eratosthenes to generate a batch of prime numbers. The difficulty in the second case is finding out
how big should the sieve be in order to generate the primes up the nth. This is solved using the Prime Number Theorem, 
and trying again with a larger sample if the first attempt was unsuccessful.

There is a "smart" function that uses the simple algorithm up to n=100 and the sieve otherwise. This offers the best 
performance for each case. The 100 number is approximate, but has been decided using the provided benchmarks. At 100, 
performance is similar for both algorithms, then it is much better for the sieve. The sieve however requires more memory
so the simple algorithm might still prove useful for some cases even if n is big.

The complexity of the simple algorithm is O(n). The sieve is better than linear, but given the benchmark values, I'd say 
it is worse than O(log n) due to the growing memory requirements. 