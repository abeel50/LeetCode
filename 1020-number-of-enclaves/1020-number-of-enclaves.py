class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        SEA, LAND = 0, 1
        ROWS, COLS = len(grid), len(grid[0])
        adjacent = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        def dfs(r, c):
            grid[r][c] = 0
            
            for dr, dc in adjacent:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= ROWS or nc < 0 or nc >=COLS or grid[nr][nc] == SEA):
                    continue
                dfs(nr, nc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == LAND and (r * c == 0 or r == ROWS - 1 or c == COLS - 1):
                    dfs(r, c)
        
        return sum([sum(r) for r in grid])
        