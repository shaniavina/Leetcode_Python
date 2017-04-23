class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.combinationSumRecu(res, [], 1, k, n)
        return res
        
    def combinationSumRecu(self, res, intermediate, start, k, target):
        if k == 0 and target == 0:
            res.append(list(intermediate))           #####??????why need list()
        if k < 0: 
            return
        while start < 10 and start * k + k * (k - 1) / 2 <= target:
            intermediate.append(start)
            self.combinationSumRecu(res, intermediate, start + 1, k - 1, target - start)
            intermediate.pop()
            start += 1
