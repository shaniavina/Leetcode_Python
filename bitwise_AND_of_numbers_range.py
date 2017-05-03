class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i, diff = 0, n - m
        while diff:
            diff >>= 1
            i += 1
        return n & m >> i << i
