class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
            
        cnt = 0    
        for i in range(len(board)):
            for j in range(len(board[0])):
                cnt += int(board[i][j] == 'X' and (i == 0 or board[i - 1][j] != 'X') and (j == 0 or board[i][j - 1] != 'X'))
        return cnt
                    
