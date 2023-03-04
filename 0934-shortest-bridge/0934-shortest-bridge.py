class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N, LAND, WATER = len(grid), 1, 0
        direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def invalid(r, c):
            return r < 0 or c < 0 or r >= N or c >= N
        
        visited = set()
        def dfs(r, c):
            if invalid(r,c) or grid[r][c] == WATER or (r, c) in visited:
                return
            visited.add((r, c))
            
            for dr, dc in direct:
                dfs(r + dr, c + dc)
        
        def bfs():
            res, q = 0, deque(visited)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direct:
                        nr, nc = r + dr, c + dc
                        if invalid(nr, nc) or (nr, nc) in visited:
                            continue
                        if grid[nr][nc]:
                            return res
                        q.append((nr, nc))
                        visited.add((nr, nc))
                res += 1
                        
        
        for r in range(N):
            for c in range(N):
                if grid[r][c] == LAND:
                    dfs(r, c)
                    return bfs()
        
            
        