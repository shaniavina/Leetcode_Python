class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:      ###without this command, time limit exceeded
            return len(s)
        dp = [[1] * len(s) for i in range(2)]
        for i in reversed(range(len(s))):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i % 2][j] = 2 + dp[(i + 1) % 2][j - 1] if i + 1 <= j - 1 else 2
                else:
                    dp[i % 2][j] = max(dp[(i + 1) % 2][j], dp[i % 2][j - 1])
        return dp[0][-1]
