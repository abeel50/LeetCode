class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adj = defaultdict(list)
        
        for i, keys in enumerate(rooms):
            adj[i] = keys
        
        q = deque([0])
        visited = set()
        
        while q:
            r = q.popleft()
            
            if r in visited:
                continue
            visited.add(r)
            
            for keys in adj[r]:
                q.append(keys)
            
            
        return len(visited) == len(rooms)
        