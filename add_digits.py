class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return (num - 1) % 9 + 1 if num >0 else 0

    ###second solution
    
     if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
