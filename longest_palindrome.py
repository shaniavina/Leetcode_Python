class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        res = 0
        for c in range(len(s)):
            if s[c] in count:
                count[s[c]] += 1
            else:
                count[s[c]] = 1
        for key in count:
            if count[key] % 2 == 0:
                res += count[key] 
            else:
                res += count[key] - 1 
        if res < len(s) :
            res += 1
        return res
        
   
