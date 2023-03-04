class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        parent = [False] * n
        
        for u, v in edges:
            parent[v] = True
            
        return [i for i in range(n) if not parent[i]] 