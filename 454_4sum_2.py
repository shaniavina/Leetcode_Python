class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ab = {}
        for i in A:
            for j in B:
                ab[i + j] = ab.get(i + j, 0) + 1
        res = 0
        for i in C:
            for j in D:
                res += ab.get(-i-j, 0)
        return res
