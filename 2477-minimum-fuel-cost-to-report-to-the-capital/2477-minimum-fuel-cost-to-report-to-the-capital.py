class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = defaultdict(list)
        for src, dst in roads:
            adj[src].append(dst)
            adj[dst].append(src)
        
        fuel = 0
        def dfs(node, parent):
            nonlocal fuel
            passangers = 0
            
            for child in adj[node]:
                if child != parent:
                    p = dfs(child, node)
                    passangers += p
                    fuel += int(ceil(p / seats))
                    
            return passangers + 1

        dfs(0, -1)
        return fuel