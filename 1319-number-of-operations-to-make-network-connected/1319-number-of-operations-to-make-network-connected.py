class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        E = len(connections)
        if E < n - 1:
            return -1
        
        adj = defaultdict(list)
        
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * n
        
        def bfs(start):
            q = deque()
            q.append(start)
            
            while q:
                cur = q.popleft()
                
                for v in adj[cur]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
        res = 0
        
        for i in range(n):
            if not visited[i]:
                res += 1
                bfs(i)
                
        return res - 1
        
        
        