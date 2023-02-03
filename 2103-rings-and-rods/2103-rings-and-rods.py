class Solution:
    def countPoints(self, rings: str) -> int:
        d = defaultdict(list)
        res = 0
        for i in range(len(rings)-1):
            c, r = rings[i: i + 2]
            d[r].append(c)
        
        return len([True for colors in d.values() if all(c in colors for c in ("R","G","B"))])

        