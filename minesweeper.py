class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        click = tuple(click)
        R, C = len(board), len(board[0])
        
        def neighbors(r, c):
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if (dr or dc) and 0 <= dr + r < R and 0 <= dc + c < C:
                        yield dr + r, dc + c
        
        stack = [click]
        seen = {click}
        
        while stack:
            r, c = stack.pop()
            
            if board[r][c] == 'M':
                board[r][c] = 'X'
            else:
                mines_adj = sum(board[nr][nc] in 'MX' for nr, nc in neighbors(r, c))
                if mines_adj:
                    board[r][c] = str(mines_adj)
                else:
                    board[r][c] = 'B'
                    for nei in neighbors(r, c):
                        if board[nei[0]][nei[1]] in 'ME' and nei not in seen:
                            stack.append(nei)
                            seen.add(nei)
        return board
