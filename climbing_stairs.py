class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        pre, cur = 1, 2
        
        for i in range(n - 1):
            temp = cur
            cur += pre
            pre = temp
        return pre
######too slow recursively
