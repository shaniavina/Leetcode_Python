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

    #####second
    class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        is_prime = [True] * n
        num = n / 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            if not is_prime[i]:
                continue
            for j in range(i * i, n, 2 * i):
                if not is_prime[j]:
                    continue
                num -= 1
                is_prime[j] = False
        return num
                
            
