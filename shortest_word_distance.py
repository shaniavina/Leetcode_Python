class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
       
        idx_1, idx_2, res = -1, -1, len(words)
        for i in range(len(words)):
            if words[i] == word1:
                idx_1 = i
            if words[i] == word2:
                idx_2 = i
            if idx_1 >= 0 and idx_2 >= 0:
                res = min(res, abs(idx_1 - idx_2))
        return res
