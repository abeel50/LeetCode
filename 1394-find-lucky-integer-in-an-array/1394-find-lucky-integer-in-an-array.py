class Solution:
    def findLucky(self, arr: List[int]) -> int:
        h = defaultdict(int)
        for n in arr:
            h[n] += 1
        return max ([k for k,v in h.items() if k == v] + [-1])        
        
        