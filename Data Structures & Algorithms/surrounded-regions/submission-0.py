class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != 'O':
                return
            
            board[row][col] = 'S'
            
            dfs(row + 1, col)
            dfs(row - 1, col) 
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            if board[row][0] == 'O':
                dfs(row, 0)
            
            if board[row][cols - 1] == 'O':
                dfs(row, cols - 1)
        
        for col in range(cols):
            if board[0][col] == 'O':
                dfs(0, col)

            if board[rows - 1][col] == 'O':
                dfs(rows - 1, col)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'S':
                    board[row][col] = 'O'
