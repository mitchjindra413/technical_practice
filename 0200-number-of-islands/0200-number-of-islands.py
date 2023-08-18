class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        
        def explore(row, col):
            key = (row, col)
            rBounds = 0 <= row < len(grid)
            cBounds = 0 <= col < len(grid[0])
            
            if not rBounds or not cBounds: return False
            if key in seen: return False
            if grid[row][col] == "0": return False
            
            seen.add(key)
            
            explore(row + 1, col)
            explore(row - 1, col)
            explore(row, col + 1)
            explore(row, col - 1)
            
            return True
        
        count = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if explore(r, c):
                    count += 1
        return count