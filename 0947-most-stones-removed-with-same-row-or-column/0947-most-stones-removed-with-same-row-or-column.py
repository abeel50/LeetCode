class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def find(x):
            if x != U[x]:
                U[x] = find(U[x])
            return U[x]

        def union(x, y):
            U.setdefault(x, x)
            U.setdefault(y, y)
            U[find(x)] = find(y)
        
        U = {}
        for i, j in stones:
            union(i, ~j)
            
        N = len(stones)
        res = N
        for x in U:
            if find(x) == x:
                res -= 1

        return res
        
        
        