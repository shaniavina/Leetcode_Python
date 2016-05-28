class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for i in reversed(s):
            if i == " ":
                if length:
                    break
            else:
                length += 1
        return length
