class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #checks if dictionery has occurence of gigits more than once
        # and also if digits is not 1-9
        def checkValid(digits):
            for k,v in digits.items():
                if k!="." and v > 1:
                    return False
            return True
        
        for i, r in enumerate(board):
            r_digits = Counter(r) #creates dict for row
            c_digits = Counter([row[i] for row in board]) #creates dict for colums
            #if any invalid digit found in ROW or COL return False
            if not checkValid(r_digits) or not checkValid(c_digits):
                return False
            
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                d = [0] * 9
                for ii in range(i, i + 3):
                    for jj in range(j, j + 3):
                        curr = board[ii][jj]
                        if curr == ".":
                            continue
                        d[int(curr) - 1] += 1
                        if d[int(curr) - 1] > 1:
                            return False
        return True
        