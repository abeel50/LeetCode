class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        def dfs(node):
            nonlocal t
            if node in visited or edges[node] == -1:
                return -1
            if time[node] != N and time[node] >= enter_time:
                return t - time[node]
            time[node] = t
            t += 1
            res = dfs(edges[node])
            visited.add(node)
            return res
        
        N = len(edges)
        visited = set()
        time = [N] * N
        res = -1
        t = 0
        for node in range(N):
            enter_time = t
            res = max(res, dfs(node))
        return res