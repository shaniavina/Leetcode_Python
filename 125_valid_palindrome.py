class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst = list(char for char in s.lower() if char.isalnum())  ###charater functions: .isalnum() and .lower()
        return lst == lst[::-1]
        
    ####second: comaprison one by one
        lst = list(char for char in s.lower() if char.isalnum())
        left, right = 0, len(lst) - 1
        while left < right:
            if lst[left] == lst[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        
