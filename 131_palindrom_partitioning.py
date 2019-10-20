class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        #time complexity: n * 2 ^ n
        # for each interval, cut or not cut --> 2 ** (n - 1)
        # for each case, to check isPal --> n
        res = []
        self.dfs(s, [], res)
        return res
    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)
                
    def isPal(self, s):
        return s == s[::-1]
