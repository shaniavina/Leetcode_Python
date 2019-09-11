class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ## binary search O(lgn)
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) / 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                r = mid
            else:
                l = mid + 1
            
