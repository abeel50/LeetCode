class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = collections.deque()
        row = len(mat)
        col = len(mat[0])
        dirs = [(-1, 0),(0, -1),(1,0),(0,1)] 
        for x in range(row):
            for y in range(col):
                if mat[x][y] == 0:
                    q.append((x,y))
                else:
                    mat[x][y] = float("inf")
        while q:
            x,y = q.popleft()
            for dx, dy in dirs:
                new_x, new_y = x+dx, y+dy
                if 0 <= new_x < row and 0 <= new_y < col and mat[new_x][new_y] > mat[x][y]+1:
                    q.append((new_x,new_y))
                    mat[new_x][new_y] = mat[x][y]+1
        return mat  
        