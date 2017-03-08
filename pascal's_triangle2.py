class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            currentRow = 2
            previous = [1, 1]
            while currentRow <= rowIndex:
                current = [1 for i in range(rowIndex + 1)]
                for i in range(1, currentRow):
                    current[i] = previous[i - 1] + previous[i]
                previous = current
                currentRow += 1
        return current

    
