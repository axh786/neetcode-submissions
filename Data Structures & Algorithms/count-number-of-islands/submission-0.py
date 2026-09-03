class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numOfIslands = 0

        def dfs(row, col):
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0 or grid[row][col] == "0":
                return
            
            grid[row][col] = "0" # mark it as 0 as we explored it 
            dfs(row + 1, col) # down
            dfs(row - 1, col) # up
            dfs(row, col + 1) # right
            dfs(row, col - 1) # left

        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    numOfIslands += 1
        
        return numOfIslands
