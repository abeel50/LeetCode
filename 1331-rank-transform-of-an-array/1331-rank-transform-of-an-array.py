from sortedcontainers import SortedSet

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        copyArr = SortedSet (arr[:])
        h = dict(zip(copyArr, range(1, len(copyArr) + 1)))
        return [h[n] for n in arr]
        