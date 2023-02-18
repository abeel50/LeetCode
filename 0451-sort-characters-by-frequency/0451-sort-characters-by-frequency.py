class Solution:
    def frequencySort(self, s: str) -> str:
        h = defaultdict(int)
        for c in s:
            h[c] += 1
        h = dict(sorted(h.items(), key=lambda item: item[1], reverse = True))
        return "".join([k * v for k, v in h.items()])
        
        