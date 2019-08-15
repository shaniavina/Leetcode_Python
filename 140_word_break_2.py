class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # memoization
        return self.wordBreakHelper(0, s, set(wordDict), {})
    def wordBreakHelper(self, k, s, wordDict, cache):
        if k == len(s):
            return []
        elif k in cache:
            return cache[k]
        else:
            cache[k] = []
            for i in range(k, len(s)):
                left = s[k: i + 1]
                if left in wordDict:
                    remainder = self.wordBreakHelper(i + 1, s, wordDict, cache)
                    if remainder:
                        for x in remainder:
                            cache[k].append(left + ' ' + x)
                    elif i == len(s) - 1:
                        cache[k].append(left)
            return cache[k]
