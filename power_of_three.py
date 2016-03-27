class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3 ** round(math.log(n, 3)) == n
        
        
        #####solution 2
        if n == 1:
            return True
        if n == 0 or n % 3 > 0:
            return False
        return self.isPowerOfThree(n / 3)
