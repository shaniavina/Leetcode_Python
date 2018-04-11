class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.helper(s, wordDict, {})
    
    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []
        res = []
        for word in wordDict:
            if not s.startswith(word): ####string.startwith(word)
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res
