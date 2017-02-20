class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        ss = (str + str)[1: -1]
        return ss.find(str) != -1
