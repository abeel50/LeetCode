class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        
        for src, dst in edges:
            adj[src].append(dst)
        
        # Retuen Max freq of color
        def dfs(node):
            if node in path:
                return float("inf")
            
            if node in visit:
                return 0

            visit.add(node)
            path.add(node)
            
            colorIndex = ord(colors[node]) - ord('a')
            count[node][colorIndex] = 1
            
            for nei in adj[node]:
                if dfs(nei) == float("inf"):
                    return float("inf")
                
                for c in range(26):
                    count[node][c] = max(count[node][c], 
                                         (1 if c == colorIndex else 0) + count[nei][c]
                                        )
            path.remove(node)
            return max(count[node])
       
        
        n, res =len(colors), 0
        visit, path = set(), set()
        count = [[0]* 26 for i in range(n)]
        
        for i in range(n):
            res = max(dfs(i), res)
        
        return -1 if res == float("inf") else res
            
                