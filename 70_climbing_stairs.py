class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            temp = b
            b = a + b
            a = temp
        return b
            
            
######too slow recursively
