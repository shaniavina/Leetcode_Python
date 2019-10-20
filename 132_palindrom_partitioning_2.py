class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # complexity: o(n ** 2)
        pal = [[False for _ in range(len(s))] for _ in range(len(s))]
        cuts = [len(s) - i - 1 for i in range(len(s))]
        for start in range(len(s) - 1, -1, -1):
            for end in range(start, len(s)):
                if s[start] == s[end] and (end - start < 2 or pal[start + 1][end - 1]):
                    pal[start][end] = True
                    if end == len(s) - 1:
                        cuts[start] = 0
                    else:
                        cuts[start] = min(cuts[start], 1 + cuts[end + 1])
        return cuts[0]
