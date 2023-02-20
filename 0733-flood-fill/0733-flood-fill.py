class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # (r,c) are index of pixels
        colored_pixels = {}
        # for right, left, up ,down
        neighbours = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        # return True if index is in range
        # false if index is out of range
        def isValidIndex(i,j):
            return (i >= 0 and i < len(image)) and (j >= 0 and j < len(image[0]))
            
        # recursive function for filing
        def rec(i, j, current_color):
            #invalid Index
            if not (isValidIndex(i,j)): return
            
            #if already filled 
            if (i,j) in colored_pixels: return
            
            # current pixel has a different color than target color
            if image[i][j] != current_color: return
            
            # sets new color
            image[i][j] = color
            
            # sets current pixel in hash
            colored_pixels[(i, j)] = True
            
            # calls for neighbours recursively
            for ix, jx in neighbours:
                rec (i+ix, j+jx, current_color)
            return 
        
        rec(sr,sc, image[sr][sc])
        return image
                    
            
        