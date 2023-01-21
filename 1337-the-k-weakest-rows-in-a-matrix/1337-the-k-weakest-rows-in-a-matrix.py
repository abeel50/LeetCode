class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        h = defaultdict(int)
        rows, cols = len(mat), len(mat[0])

        for r in range(rows):
            h[r] = sum(mat[r])
        
        h = {k: v for k, v in sorted(h.items(), key=lambda item: item[1])}
        return list(h.keys())[:k]

        