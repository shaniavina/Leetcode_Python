class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        result = []
        self.combineRecu(n, result, 0, [], k)
        return result
    
    def combineRecu(self, n, result, start, intermediate, k):
        if k == 0:
            result.append(intermediate[:])
        for i in xrange(start, n):
            intermediate.append(i + 1)
            self.combineRecu(n, result, i + 1, intermediate, k - 1)
            intermediate.pop()
