class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        
        board = [["."] * n for i in range(n)]
        res = 0
        
        def backTrack(row):
            nonlocal res
            if row == n:
                res += 1
                return
            
            for c in range(n):
                if c in col or (row + c) in posDiag or (row - c) in negDiag:
                    continue
                
                # add positions to required sets
                # check out QUEEN moves
                col.add(c)
                posDiag.add(row + c)
                negDiag.add(row - c)
                board[row][c] = "Q"
                
                backTrack(row + 1)
                
                # because we're bruteforcing
                col.remove(c)
                posDiag.remove(row + c)
                negDiag.remove(row - c)
                board[row][c] = "."
        
        backTrack(0)
        return res
        