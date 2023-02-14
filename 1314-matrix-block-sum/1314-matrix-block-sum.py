class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        
        pre = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        
        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                pre[i][j] = (pre[i - 1][j] + pre[i][j - 1] 
                              - pre[i - 1][j - 1]+ mat[i - 1][j - 1])
        
        def get(i, j):
            i = max(min(ROWS, i), 0)
            j = max(min(COLS, j), 0)
            return pre[i][j]
        
        res = [[0] * COLS for _ in range(ROWS)]
        for i in range(ROWS):
            for j in range(COLS):
                res[i][j] = (
                    get(i + k + 1, j + k + 1)
                    - get(i + k + 1, j - k)
                    - get(i - k, j + k + 1)
                    + get(i - k, j - k)
                )
        return res