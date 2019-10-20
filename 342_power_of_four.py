class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num % 4 == 0:
            num /= 4
        return num == 1
        
        #######second solution
        ###(0x55555555) <==> 1010101010101010101010101010101
        return num > 0 and num & (num - 1) == 0 and num & 0x55555555 == num
