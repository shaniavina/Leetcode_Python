class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        int_max = 2 ** 31 - 1
        int_min = -2 ** 31
        res = 0
        if not str:
            return res
        i = 0
        ### string.strip() to remove leading or traling 0s
        while i < len(str) and str[i] == ' ':
            i += 1
        sign = 1
        
        ### always make sure i is within len(str)
        if i < len(str) and str[i] == '+':
            i += 1
        elif i < len(str) and str[i] == '-':
            i += 1
            sign = -1
        while i < len(str) and str[i] >= '0' and str[i] <= '9':
            if int_max < 10 * res + ord(str[i]) - ord('0'):
                return int_max if sign > 0 else int_min
            res = 10 * res + ord(str[i]) - ord('0')
            i += 1
        return sign * res
