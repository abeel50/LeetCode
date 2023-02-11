class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Maps stops to routes
        stops = defaultdict(set)
        
        # stops:(0,1,2,....)
        for i, r in enumerate(routes):
            for stop in r:
                stops[stop].add(i)
                
        # sets to save stops and routes to avoid repeattaion
        visitedStops, visitedRoutes = set(), set()
        #queue for BFS
        q = deque([source])
        visitedStops.add(source)
        
        res = 0
        
        while q:
            
            for _ in range(len(q)):
                stop = q.popleft()
                
                if stop == target:
                    return res
                
                # realted routes of specific stops
                for routeID in stops[stop]:
                    if routeID not in visitedRoutes:
                        for newStop in routes[routeID]:
                                q.append(newStop)
                                visitedStops.add(newStop)
                        visitedRoutes.add(routeID)
                    
            res += 1

        return -1
        