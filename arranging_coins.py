class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        return int((math.sqrt(8 * n + 1) - 1) / 2)   ##equations
   #####second solution
   left, right = 1, n
        while left <= right:
            mid = left + (right - left) / 2
            if 2 * n < (mid + 1) * mid:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1
