class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        z = 1
        
        while z <= num:
            z = z << 1
        return (z-1) ^ num
