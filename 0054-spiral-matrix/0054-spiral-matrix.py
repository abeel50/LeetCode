class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        while left < right and top < bottom:
            
            # get every element in top row "---->"
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            # get every ele in right col "|"
            #                            "|"
            #                            "v"
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1
            
            # if matrix is only row matrix or only col matrix
            # "[0,0,0,0]" or same row in shape of col
            # we break the loop (spiral is not possible further)
            if not (left < right and top < bottom):
                break
                
            # get every el in bottom row  "<----"
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            
            # get every elem in left col "^"
            #                            "|"
            #                            "|"            
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            
        return res