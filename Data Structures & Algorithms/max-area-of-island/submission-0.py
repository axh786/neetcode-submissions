class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        def dfs(row, col):
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0 or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            area = 1
            
            area += dfs(row + 1, col)
            area += dfs(row - 1, col)
            area += dfs(row, col + 1)
            area += dfs(row, col - 1)

            return area
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    maxArea = max(maxArea, area)
        
        return maxArea
