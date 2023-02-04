class Solution:
    def digitCount(self, num: str) -> bool:
        h = defaultdict(int)
        for n in num:
            h[int(n)] += 1
        for i, n in enumerate(num):
            if h.get(i, 0) != int(n):
                return False
        return True
            
        