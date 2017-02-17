class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        n = abs(num)
        while n:
            res += str(n % 7)
            n /= 7
        return ['', '-'][num < 0] + res[::-1] or '0'
