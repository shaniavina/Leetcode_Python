class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        abs_n = abs(n)
        while abs_n:
            if abs_n & 1:   ##one step; two step
                res *= x
            abs_n >>= 1
            x *= x
        return 1 / res if n < 0 else res
    
    
    
