class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        for row in range(len(grid) -1, -1, -1):
            for col in range(len(grid[0]) -1, -1, -1):
                if row == len(grid) - 1 and col == len(grid[0]) - 1: 
                    continue
                d = grid[row + 1][col] if row + 1 < len(grid) else float('inf')
                r = grid[row][col + 1] if col + 1 < len(grid[0]) else float('inf')
                grid[row][col] = grid[row][col] + min(d, r)
        
        return grid[0][0]