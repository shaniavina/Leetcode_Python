class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
         if num == 0:
            return '0'   ####not in the loop
        n, res = abs(num), ''    ###consider sign
        while n:
            res = str(n % 7) + res    ###reverse the string
            n /= 7
        
        return res if num > 0 else '-' + res
