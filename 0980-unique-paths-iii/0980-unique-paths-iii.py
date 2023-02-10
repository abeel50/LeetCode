class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res , nonObstacles = 0, 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(r, c, count):
            if (r < 0 or r >= ROWS) or (c < 0 or c >= COLS) or (grid[r][c] == -1):
                return
            
            nonlocal res
            if grid[r][c] == 2:
                if nonObstacles == count:
                    res += 1
                return
            
            #makes grid visited
            grid[r][c] = -1
            
            for dr, dc in directions:
                dfs(r + dr, c + dc, count + 1)
            grid[r][c] = 0
            
            
        startRow, startCol = 0, 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    startRow, startCol = r, c
                elif grid[r][c] == 0:
                    nonObstacles += 1
                
        dfs(startRow, startCol, 0)
        return res
        