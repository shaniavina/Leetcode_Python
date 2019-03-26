class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x_copy, reverse = x, 0
        while x_copy:
            reverse = reverse * 10 + x_copy % 10
            x_copy /= 10
        return x == reverse

    
