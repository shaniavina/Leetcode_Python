class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = collections.Counter()
        best = i = 0
        for j in range(len(s)):
            count[s[j]] += 1
            best = max(best, count[s[j]])
            if best + k < j - i + 1:
                count[s[i]] -= 1
                i += 1
        return len(s) - i
