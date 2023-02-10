class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        obstacle = -1
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = obstacle
    

        # set destionation to 1
        obstacleGrid[m-1][n-1] = 1
        
        #bottom up
        for r in range(m-1, -1 ,-1):
            for c in range(n-1, -1 , -1):
                if obstacleGrid[r][c] == obstacle:
                    continue
                #check right
                if c + 1 < n and obstacleGrid[r][c + 1] != obstacle:
                    obstacleGrid[r][c] += obstacleGrid[r][c + 1]
                #check down
                if r + 1 < m and obstacleGrid[r+1][c] != obstacle:
                    obstacleGrid[r][c] += obstacleGrid[r+1][c]
        return obstacleGrid[0][0]
        