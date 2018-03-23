class Solution(object):
    ###top down DFS, using memoization to decrease O(n!) to O(2^n)
    def helper(self, allowed, target, so_far):
        if len(allowed) == 0:
            return False
        state = tuple(allowed)  ###tuple or string
        if state in self.memo:
            return self.memo[state]
        else:
            self.memo[state] = False
            if max(allowed) + so_far >= target:
                self.memo[state] = True
            else:
                for x in allowed:
                    new_allowed = [y for y in allowed if x!=y]
                    if self.helper(new_allowed, target, so_far+x) == False:
                        self.memo[state] = True
                        break
            return self.memo[state]
    
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        allowed = [x for x in range(1, maxChoosableInteger+1)]
        if sum(allowed) < desiredTotal:
            return False
        self.memo = {}
        return self.helper(allowed, desiredTotal, 0)
