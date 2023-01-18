class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = sum([mat[i][i] for i in range(len(mat))]) + sum([mat[i][j] for i, j in zip(range(len(mat)),range(len(mat)-1,-1,-1))])
        if len(mat) % 2 != 0:
            mid = len(mat) // 2
            s -= mat[mid][mid] 
            
        return s
        