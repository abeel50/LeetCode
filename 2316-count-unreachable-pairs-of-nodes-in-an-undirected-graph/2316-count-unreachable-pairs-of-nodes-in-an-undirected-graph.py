class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(lambda:set())
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = set()
        prev_vis = 0
        
        def dfs(node):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)
            return 
        
        res = 0
        total = n
        for i in range(n):
            if i not in visited:
                dfs(i)
                count = len(visited)-prev_vis
                total -= count 
                res += count*total
                prev_vis = len(visited)
        return res
            