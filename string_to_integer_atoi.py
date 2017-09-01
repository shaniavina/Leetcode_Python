class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX =  2 ** 31 - 1
        INT_MIN = -2 ** 31
        result = 0
        
        if not str:
            return result
        
        i = 0
        while i < len(str) and str[i] == ' ':
            i += 1
        
        sign = 1
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            i += 1
            sign = -1
        
        while i < len(str) and str[i] >= '0' and str[i] <= '9':
            if INT_MAX < 10 * result + ord(str[i]) - ord('0'):
                return INT_MAX if sign > 0 else INT_MIN
            result = result * 10 + ord(str[i]) - ord('0')
            i += 1
        return sign * result
