class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        SIZE = len(matrix)
        if SIZE == 0: return 0
        
        for r in range(SIZE - 2, -1, -1) :
            for c in range(SIZE):

                best = matrix[r + 1][c]
                if c > 0 :
                    best = min(best, matrix[r + 1][c - 1])
                if c + 1 < SIZE :
                    best = min(best, matrix[r + 1][c + 1])
                matrix[r][c] = matrix[r][c] + best
        
        return min([matrix[0][i] for i in range(SIZE)])