class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h = defaultdict(int)
        for n in arr:
            h[n] += 1
        return len(set(h.values())) == len(h.values())
        