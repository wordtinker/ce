"""
SUM OF PRIMES
CHALLENGE DESCRIPTION:

Write a program which determines the sum of the first 1000 prime numbers.

INPUT SAMPLE:

There is no input for this program.

OUTPUT SAMPLE:

Print to stdout the sum of the first 1000 prime numbers.

3682913
"""


class Prime:

    def __init__(self, n):
        self.n = n
        self.i = 1

    def __iter__(self):
        self.p = 2
        self.primes = [2]
        return self

    def __next__(self):
        if self.i > self.n:
            raise StopIteration

        self.p += 1

        is_prime = True
        for p in self.primes:
            if self.p % p == 0:
                is_prime = False
                break

        if is_prime:
            prime = self.primes[-1]
            self.primes.append(self.p)
            self.i += 1
            return prime
        else:
            return self.__next__()


s = 0
for x in Prime(1000):
    s += x
print(s)
