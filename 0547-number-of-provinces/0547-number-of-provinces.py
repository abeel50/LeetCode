class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        SIZE = len(isConnected)
        visited = set()
        
        def dfs(city):
            visited.add(city)
            
            for end in range(SIZE):
                if isConnected[city][end] and end not in visited:
                    dfs(end)
        
        provinces = 0
        for city in range(SIZE):
            if city not in visited:
                provinces += 1
                dfs(city)
            
        return provinces
                   