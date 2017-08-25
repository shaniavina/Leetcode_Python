class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = int(len(s) and s[-1] != ' ')
        for i in range(1, len(s)):
            if s[i] == ' ' and s[i - 1] != ' ':
                result += 1
        return result

    
