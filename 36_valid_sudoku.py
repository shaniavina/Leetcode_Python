class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        ###just make sure there is unique value in each row, each col, each square
        return self.isValidRow(board) and self.isValidCol(board) and self.isValidSquare(board)
    
    def isValidRow(self, board):
        for row in board:
            if not self.isValidUnit(row):
                return False
        return True
    def isValidCol(self, board):
        for col in zip(*board):
            if not self.isValidUnit(col):
                return False
        return True
    def isValidSquare(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.isValidUnit(square):
                    return False
        return True
    def isValidUnit(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)
