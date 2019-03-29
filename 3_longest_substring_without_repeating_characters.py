class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        start = maxLength = 0
        lookup = {}
        for i in range(len(s)):
            if s[i] in lookup and start <= lookup[s[i]]:
                start = lookup[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            lookup[s[i]] = i
        return maxLength
