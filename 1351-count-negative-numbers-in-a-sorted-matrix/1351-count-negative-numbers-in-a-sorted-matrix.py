class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        res = 0
        for i, row in enumerate(grid):
            for j in range(len(row)-1,-1,-1):
                if grid[i][j] < 0:
                    res += 1
                else:
                    break
        return res
                
        