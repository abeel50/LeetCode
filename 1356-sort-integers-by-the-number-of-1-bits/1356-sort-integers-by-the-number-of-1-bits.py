class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        h = defaultdict(int)
        
        for i,n in enumerate(arr):
            h[(i,n)] = sum ([int(x) for x in bin(n)[2:] if x == "1"])
        h = {k: v for k, v in sorted(h.items(), key=lambda item: item[1])}
        
        return [n for(i,n) in h.keys() ]
        
        