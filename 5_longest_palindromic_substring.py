class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in range(len(s)):
            for k in range(2):
                tmp = self.helper(s, i, i + k)  #####odd and even
                if len(tmp) > len(res):
                    res = tmp
        return res
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]
        
        
        #######second
        
     class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # ###when you increase s by 1 character, you could only increase maxPalindromeLen by 1 or 2
        # if not s:
        #     return None
        # maxLen = 1
        # start = 0
        # for i in range(1, len(s)):
        #     if i - maxLen >= 1 and s[i - maxLen - 1 : i + 1] == s[i - maxLen - 1 : i + 1][::-1]:
        #         start = i - maxLen - 1
        #         maxLen += 2
        #         continue
        #     if i - maxLen >= 0 and s[i - maxLen : i + 1] == s[i - maxLen : i + 1][::-1]:
        #         start = i - maxLen
        #         maxLen += 1
        # return s[start : start + maxLen]
        
        
        
        
        #Manacher algorithm in Python O(n)
       # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        t = '#'.join('^{}$'.format(s))
        n = len(t)
        p = [0] * n
        center = radius = 0
        for i in range (1, n - 1):
            if radius > i:
                p[i] = min(radius - i, p[2*center - i]) 
            # Attempt to expand palindrome centered at i
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + p[i] > radius:
                center, radius = i, i + p[i]
    
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(p))
        return s[(centerIndex  - maxLen)/2: (centerIndex  + maxLen)/2]
    
