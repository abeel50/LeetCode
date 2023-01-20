class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #(row, col) for key tuple
        islands= defaultdict(int)
        
        # for right, left, up ,down
        neighbours = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        # return True if index is in range otherwise false 
        def isValidIndex(i,j):
            return (i >= 0 and i < len(grid)) and (j >= 0 and j < len(grid[0]))
        
        def rec(i, j, pi, pj):
            #if already filled 
            if (i,j) in islands: return
            
            # if water return
            if grid[i][j] == 0: return
            
            # if it's first land piece
            if pi == -1 and pj == -1:
                islands[(i,j)] += 1
            else:
                # increments size
                islands[(pi,pj)] += 1
                # because parent and child are connected now it will 1+1
                islands[(i,j)] = islands[(pi, pj)]

            # calls for neighbours recursively
            for ix, jx in neighbours:
                new_i , new_j = i+ix, j+jx
                #checks if index is valid 
                if isValidIndex(new_i, new_j):
                    #recursion to new function
                    rec (new_i , new_j, i ,j)
                    #update parent's count of lands
                    #because islands are connected
                    if (new_i , new_j) in islands:
                        islands[(i,j)] = max(islands[(new_i , new_j)],  islands[(i,j)])
            return
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    rec(i,j ,-1,-1)
                    
        
        return max(islands.values()) if len(islands) > 0 else 0
                
            
        