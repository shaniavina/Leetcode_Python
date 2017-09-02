class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []
        self.dfs(s, [])
        return self.res

    def dfs(self, s, path):
        if not s:
            self.res.append(list(path))
        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path + [s[:i]])   ###can only concatenate list; [[]]
    def isPal(self, s):
        return s == s[::-1]
    
 
