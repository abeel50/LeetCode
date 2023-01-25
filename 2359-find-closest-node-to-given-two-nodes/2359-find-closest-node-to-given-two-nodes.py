class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # adjency Matrix
        adj = defaultdict(list)
        
        for i, dst in enumerate(edges):
            adj[i].append(dst)
        
        def bfs(src, distMap):
            q = deque()
            q.append([src, 0]) # for prevention of cycles
            distMap[src] = 0
            
            while q:
                node , dist = q.pop()
                
                # get the neighbours of current node
                for nei in adj[node]:
                    if nei not in distMap: # if not checked will go to an infinite loop
                        q.append([nei, dist + 1]) # appedning to queue adding 1 to dist
                        distMap[nei] = dist + 1
        
        
        # dist hash maps for both nodes
        n1Dist, n2Dist= {}, {}
        
        # bfs for both nodes
        bfs(node1, n1Dist)
        bfs(node2, n2Dist)
        
        res = -1
        resDist = float('inf')
        for i in range(len(edges)):
            # if edge is reachable from both nodes
            if i in n1Dist and i in n2Dist:
                dist = max(n1Dist[i], n2Dist[i])
                if dist < resDist:
                    res = i
                    resDist = dist
        return res
                