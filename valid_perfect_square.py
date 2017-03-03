class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        
        """
        if num <= 1:
            return True
        left, right = 1, num
        while left <= right:
            mid = left + (right - left) / 2
            if mid >= num / mid:
                right = mid - 1
            else:
                left = mid + 1
        return left * left == num
