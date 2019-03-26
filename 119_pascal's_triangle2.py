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
    
#####second 
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]    ####local variable 'result' referenced before assignment
        for i in range(1, rowIndex + 1):
            result = [1] + [result[j - 1] + result[j] for j in range(1, i)] + [1]
        return result
