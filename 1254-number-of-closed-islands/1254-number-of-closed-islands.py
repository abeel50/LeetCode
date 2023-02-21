class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        LAND, WATER = 0, 1
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
   
        def dfs(r, c):        
            grid[r][c] = 1
            for dr , dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == WATER:
                    continue
                dfs(nr, nc)
                
        # Remove lands connected to edge
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == LAND and (r * c == 0 or r == ROWS - 1 or c == COLS - 1):
                    dfs(r, c)
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == LAND:
                    dfs(r, c)
                    res += 1
        return res
        