class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {}
        for char in s:
            if char in lookup:
                lookup[char] += 1
            else:
                lookup[char] = 1
        for i in range(len(s)):
            if lookup[s[i]] == 1:
                return i
        return -1
