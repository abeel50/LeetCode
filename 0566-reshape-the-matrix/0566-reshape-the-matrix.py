class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) == r  and len(mat[0]) == c:
            return mat
        
        if r * c != len(mat) * len(mat[0]):
            return mat
        
        R, C = 0, 0
        res =  [[0 for _ in range(c)] for _ in range(r)]
        
        for i in mat:
            for j in i:
                if C == c:
                    R += 1
                    C = 0
                res[R][C] = j
                C += 1
        return res
            
        