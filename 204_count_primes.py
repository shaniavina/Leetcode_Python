class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
         #####second
        if n <= 2:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):    ####integer
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False
        return sum(primes)

    