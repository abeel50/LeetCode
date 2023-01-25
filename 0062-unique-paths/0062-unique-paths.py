class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 2d dp grid
        grid = [[0 for _ in range(n)] for _ in range(m)]
        
        # set destionation to 1
        grid[m-1][n-1] = 1
        
        #bottom up
        for r in range(m-1, -1 ,-1):
            for c in range(n-1, -1 , -1):
                #check right
                if c + 1 < n:
                    grid[r][c] += grid[r][c + 1]
                #check down
                if r + 1 < m:
                    grid[r][c] += grid[r+1][c]
        return grid[0][0]
        
        