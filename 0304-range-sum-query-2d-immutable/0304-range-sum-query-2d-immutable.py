class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.preMat = [[0]* (COLS + 1) for _ in range(ROWS + 1)]
        
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.preMat[r][c + 1]
                self.preMat[r + 1][c + 1] = prefix + above
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 +1, col2 + 1
        bottomRight = self.preMat[r2][c2]
        above = self.preMat[r1 -1][c2]
        left = self.preMat[r2][c1 -1]
        topLeft = self.preMat[r1 - 1][c1 - 1]
        
        return bottomRight - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)