class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(1, rowIndex + 1):
            row = [1] + [row[k] + row[k + 1] for k in range(len(row) - 1)] + [1]
        return row
        
       
