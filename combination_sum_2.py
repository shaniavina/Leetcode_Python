class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.combinationSum2Recu(sorted(candidates), result, 0, [], target)
        return result
        
    def combinationSum2Recu(self, candidates, result, start, intermediate, target):
        if target == 0:
            result.append(list(intermediate))
        pre = 0
        while start < len(candidates) and candidates[start] <= target:
            if pre != candidates[start]:
                intermediate.append(candidates[start])
                self.combinationSum2Recu(candidates, result, start + 1, intermediate, target - candidates[start])
                intermediate.pop()
                pre = candidates[start]
            start += 1
