class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result, dvd = '', n   ####the result should be a string, not a list
        
        while dvd:
            result += chr(ord('A') + (dvd - 1) % 26)
            dvd = (dvd - 1) / 26
        return result[::-1]
