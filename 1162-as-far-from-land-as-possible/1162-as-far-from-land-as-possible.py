class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque()
        
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    q.append((r, c))
        res = -1
        directions =[(0, 1), (1, 0), (0,-1), (-1,0)]
        while q:
            r, c = q.popleft()
            res = grid[r][c]
            for dr, dc in directions:
                nr ,nc = dr + r, dc + c
                if (min(nr, nc) >= 0 and max(nr, nc) < N and
                    grid[nr][nc] == 0):
                    q.append((nr, nc))
                    grid[nr][nc] = grid[r][c] + 1
                
            
        
        return res - 1 if res > 1 else -1
        