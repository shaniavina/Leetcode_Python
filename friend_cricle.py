class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        seen = set()
        
        def dfs(node):
            for i, j in enumerate(M[node]):
                if j and i not in seen:
                    seen.add(i)
                    dfs(i)
        ans = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans
