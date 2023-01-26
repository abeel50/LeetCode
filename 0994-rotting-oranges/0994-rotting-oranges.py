class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # if grid is empty
        if not grid: return -1
        
        q = deque()
        fresh, minutes = 0, 0
        # number of rows and cols in grid
        ROWS, COLS = len(grid), len(grid[0])
                            
        #iterate through grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        # for right, left, up ,down 
        neighbours = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        while q and fresh > 0:
            
            for i in range(len(q)):
                # pop from front
                r, c = q.popleft()
            
                # check neighbours
                for nr, nc in neighbours:
                    rx , cx = r + nr , c + nc
                    # if neighbour is in valid range 
                    # if neighbour is land and has not been visited yet
                    if (rx in range(ROWS)) and (cx in range(COLS)) and (grid[rx][cx] == 1) :
                        q.append((rx, cx)) #append to queue
                        grid[rx][cx] = 2
                        fresh -= 1
            minutes += 1
        
        
        return minutes if fresh == 0 else -1
        