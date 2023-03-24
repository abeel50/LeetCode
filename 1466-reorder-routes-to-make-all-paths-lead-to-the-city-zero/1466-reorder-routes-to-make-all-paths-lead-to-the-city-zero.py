class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        outward = set()
        visited = [False] * n
        
        def dfs(city):
            visited[city] = True
            
            for nei in adj[city]:
                if not visited[nei]:
                    outward.add((city, nei))
                    dfs(nei)
        dfs(0)
        res = 0
        for u,v in connections:
            if (u, v) in outward:
                res += 1
        return res
            
        