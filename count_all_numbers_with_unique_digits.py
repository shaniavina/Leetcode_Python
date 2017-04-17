class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        count, fk = 10, 9
        for k in range(2, n + 1):
            fk *= 10 - k + 1      ########f(k) = count of numbers with unique digits with length equals k.
            count += fk
        return count
