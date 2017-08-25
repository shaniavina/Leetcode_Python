class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = []
        for c in s:
            if c in ['a','e','i','o','u','A','E','I','O','U']:###upper, lower case
                vowels.append(c)
        for i in range(len(s)):
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                s[i] = vowels.pop()
        return ''.join(s)
