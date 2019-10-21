class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        R, C = len(board), len(board[0])
        if R <= 2 or C <= 2:
            return
        queue = []
        for r in range(R):
            queue.extend([(r, 0), (r, C - 1)])
        for c in range(C):
            queue.extend([(0, c), (R - 1, c)])
        while queue:
            r, c = queue.pop(0)
            if 0 <= r < R and 0 <= c < C and board[r][c] == 'O':
                board[r][c] = 'N'
                queue.extend([(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)])
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'N':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'
        
        
