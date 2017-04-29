class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(n):
            for j in reversed(res):      
                res.append(1 << i | j)      ####rules
        return res
