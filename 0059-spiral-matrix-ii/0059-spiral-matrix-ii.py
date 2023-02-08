class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for j in range(n)]
        left, right = 0, n
        top, bottom = 0, n
        
        data = 1
        
        while left < right and top < bottom:
            
            # get every element in top row "---->"
            for i in range(left, right):
                res[top][i] = data
                data += 1
            top += 1
            
            # get every ele in right col "|"
            #                            "|"
            #                            "v"
            for i in range(top, bottom):
                res[i][right-1] = data
                data += 1
            right -= 1
            
            # if matrix is only row matrix or only col matrix
            # "[0,0,0,0]" or same row in shape of col
            # we break the loop (spiral is not possible further)
            if not (left < right and top < bottom):
                break
                
            # get every el in bottom row  "<----"
            for i in range(right - 1, left - 1, -1):
                res[bottom-1][i] = data
                data += 1
            bottom -= 1
            
            # get every elem in left col "^"
            #                            "|"
            #                            "|"            
            for i in range(bottom - 1, top - 1, -1):
                res[i][left] = data
                data +=1
            left += 1
            

        
        return res
        