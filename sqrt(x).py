class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x in (0, 1):
            return x
        left, right = 1, x / 2   ####can not starting from 0 since we have it as nominator
        while left <= right:
            mid = left + (right - left) / 2   ####write in this way: overflow!
            if mid > x / mid:      
                right = mid - 1
            else:
                left = mid + 1
        return left - 1
    
  
