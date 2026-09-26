class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in board:
            rowSet = set()
            for element in row:
                if element in rowSet:
                    return False
                
                if element != ".":
                    rowSet.add(element)

        for i in range(9):
            colSet = set()
            for j in range(9):
                if board[j][i] in colSet:
                    return False
                
                if board[j][i] != ".":
                    colSet.add(board[j][i])
        
        for row in range(0, 9, 3): # 0 3 6 
            for col in range(0, 9, 3):
                boxSet = set()
                for boxRow in range(row, row + 3): # iterates to the row + 3 so for the first 0 1 2
                    for boxCol in range(col, col + 3): # iterates to the col so for the first 0 1 2
                        if board[boxRow][boxCol] in boxSet:
                            return False
                        
                        if board[boxRow][boxCol] != ".":
                            boxSet.add(board[boxRow][boxCol])
        
        return True
