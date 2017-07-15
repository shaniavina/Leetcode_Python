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
        
   
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # counter = {}
        # add_one = False
        # res = 0
        # for i in s:
        #     if i in counter:
        #         counter[i] += 1
        #     else:
        #         counter[i] = 1
        # for key in counter:
        #     if counter[key] % 2:
        #         add_one = True
        #         res += counter[key] - 1
        #     else:
        #         res += counter[key]
        # if add_one:
        #     res += 1
        # return res
        
        #####collections
        odds = 0
        for k, v in collections.Counter(s).iteritems():
            odds += v & 1
        return len(s) - odds + int(odds > 0)
