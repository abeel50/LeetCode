class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkValid(digits):
            for k,v in digits.items():
                if k!="." and (int(k) > 9 or int(k) < 1):
                    return False
                if k !="." and v > 1 and int(k) in range(1,10):
                    return False
            return True
        
        
        for i, r in enumerate(board):
            r_digits = Counter(r)
            c_digits = Counter([row[i] for row in board])
            if not checkValid(r_digits) or not checkValid(c_digits):
                return False
            
        r, c = 0, 0
        for k in range(1,10):
            d = defaultdict(int)
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    curr = board[i][j]
                    if curr == ".":
                        continue
                    d[curr] += 1
                    if d[curr] > 1:
                        return False
            
            if k % 3 == 0:
                r = 0
                c += 3
            else:
                r+= 3
            
    
        return True
        