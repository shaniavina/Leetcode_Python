class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        k, res = 5, 0
        while k <= n:
            res += n / k
            k *= 5
        return res
