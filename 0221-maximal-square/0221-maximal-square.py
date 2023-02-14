class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        # each (r,c) -> maxLength
        cache = {}
        res = float('-inf')
        
        def rec(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            
            if (r,c) not in cache:
                down = rec(r + 1, c)
                right = rec(r, c + 1)
                diag = rec(r + 1, c + 1)
                
                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)
            
            nonlocal res
            res = max(res, cache[(r, c)])
            return cache[(r, c)]
        
        rec(0, 0)
        return res ** 2
        # return max(cache.values()) ** 2
        