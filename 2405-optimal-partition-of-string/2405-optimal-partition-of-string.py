class Solution:
    def partitionString(self, s: str) -> int:
        res = 0
        h = defaultdict(int)
        
        for c in s:            
            if c in h:
                h.clear()
                res += 1
            h[c] += 1
        if len(h) > 0:
            res += 1
        return res