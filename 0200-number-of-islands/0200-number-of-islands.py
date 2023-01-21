class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if grid is empty
        if not grid: return 0
        
        # number of rows and cols in grid
        rows, cols = len(grid), len(grid[0])
        
        # to keep track of visited nodes
        visit = set()
        # total number of islands
        islands = 0
        
        # BFS
        def bfs(r, c):
            # Queue
            q = collections.deque()
            # add to visited 
            visit.add((r, c))
            # append to queue
            q.append((r, c))
            
            # until queu is not empty
            while q:
                # pop from front
                # if we replace popleft() with pop() then it will be a DFS
                row, col = q.popleft()
            
                # for right, left, up ,down 
                neighbours = [(0, 1), (0, -1), (-1, 0), (1, 0)]
                # check neighbours
                for nr, nc in neighbours:
                    rx , cx = row + nr , col + nc
                    # if neighbour is in valid range 
                    # if neighbour is land and has not been visited yet
                    if (rx in range(rows)) and (cx in range(cols)) and (grid[rx][cx] == "1") and ((rx, cx) not in visit):
                        q.append((rx, cx)) #append to queue
                        visit.add((rx, cx)) # add to vitis
                        
        
        #iterate through grid
        for r in range(rows):
            for c in range(cols):
                # if specific location is land and already not visited
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands