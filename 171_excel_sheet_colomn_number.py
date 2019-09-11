class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for char in s:
            res *= 26
            res += ord(char) - ord('A') + 1
        return res

    #### second
    
    s = s[::-1]
        res = 0
        for power, char in enumerate(s):
            res += (ord(char) - ord('A') + 1) * (26 ** power)
        return res
