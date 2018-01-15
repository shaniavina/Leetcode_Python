# Time:  O(n)
# Space: O(1)

class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestWordDistance(self, words, word1, word2):
        idx, res = -1, float('inf')
        for i in range(len(words)):
            if words[i] == word1 or words[i] == word2:
                if (idx != -1 and (word1 == word2 or words[i] != words[idx])):
                    res = min(res, i - idx)
                idx = i
        return res            
