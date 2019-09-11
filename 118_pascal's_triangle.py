class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res, row = [], [1]
        for i in range(numRows):
            res.append(row)
            row = [1] + [row[k] + row[k + 1] for k in range(len(row) - 1)] + [1]
        return res
