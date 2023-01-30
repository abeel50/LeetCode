class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for start, end in intervals:
            if res and res[-1][1] >= start:
                res[-1] = [min(start, res[-1][0]), max(end, res[-1][1])]
            else:
                res.append([start, end])
        return res
        