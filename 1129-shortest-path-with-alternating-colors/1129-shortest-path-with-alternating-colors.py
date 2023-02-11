class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        
        # 0 - red, 1 - blue
        for u, v in redEdges:
            adj_list[u].append((v, 0))
        for u, v in blueEdges:
            adj_list[u].append((v, 1))
        
        # (node, last_color), start with red and blue pills
        q = deque([(0,0),(0,1)]) 
        
        dist = [float(inf)] * n
        visited = set()
        level = 0
        
        while q:
            for _ in range(len(q)):
                node, last_color = q.popleft()
                dist[node] = min(dist[node], level)

                for nei, edge_color in adj_list[node]:
                    if last_color != edge_color and (nei, edge_color) not in visited:
                        visited.add((nei, edge_color))
                        q.append((nei, edge_color))
            level += 1
        
        return [d if d != float(inf) else -1 for d in dist]