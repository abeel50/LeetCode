class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid2), len(grid2[0])
        WATER, LAND, VISITED = 0, 1, 2
        
        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >=COLS or grid2[r][c] != LAND):
                    return 1
            grid2[r][c] = VISITED
            
            return( dfs(r + 1, c) & dfs(r - 1, c) & 
                    dfs(r, c + 1) & dfs(r, c - 1) & grid1[r][c] )              
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == LAND:
                    res += dfs(r, c)
        return res
            
        