class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        res = -1
        h = defaultdict(int)
        c = defaultdict(int)
        
        for t in trust:
            ai, bi = t[0], t[1]
            h[ai] = bi
            c[bi] += 1
        
        for p in range(1, n+1):
            if p not in h and c[p] == n-1:
                return p
        return res
            
            
            
        
            
            
            
        