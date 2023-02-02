class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        SIZE = len(grid)
        # (r,c, length of path)
        q = deque([(0, 0, 1)])
        
        # to keep track of viaited index
        # (row, colum)
        visited = set((0, 0))
        
        #8-directionally connected 
        directions =[(0, 1), (1, 0), (0, -1), (-1, 0),
                     (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
        while q:
            r, c, length = q.popleft()
            # if current position is out of grid
            # or current position is 1
            if min(r, c) < 0 or max(r, c) >= SIZE or grid[r][c] == 1:
                continue
                
            # if reached at destination
            if r == SIZE - 1 and c == SIZE - 1:
                return length
            #check it's eight directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited:
                    q.append((nr, nc, length + 1))
                    visited.add((nr, nc))
        return -1
                