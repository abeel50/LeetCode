class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        h = OrderedDict()
        
        for c in arr:
            h[c] = 1 + h.get(c, 0)
        distinct = [k for k,v in h.items() if v == 1]
        return "" if k > len(distinct) else distinct[k-1]