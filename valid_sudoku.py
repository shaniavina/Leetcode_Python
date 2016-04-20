class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        ##check rows
        
        for i in range(9):
            nSet = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] not in nSet:
                        nSet.add(board[i][j])
                    else:
                        return False
        ##check cols
        
        for i in range(9):
            nSet = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] not in nSet:
                        nSet.add(board[j][i])
                    else:
                        return False
        ##check sub square
        for i in range(3):
            for j in range(3):
                nSet = set()
                for m in range(3):
                    for n in range(3):
                        x = i * 3 + m
                        y = j * 3 + n
                        if board[x][y] != '.':
                            if board[x][y] not in nSet:
                                nSet.add(board[x][y])
                            else:
                                return False
        return True
