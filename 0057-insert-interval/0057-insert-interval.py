class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        def doesIntervalsOverlap(a:List[int], b:List[int]):
            return min(a[1], b[1]) - max(a[0], b[0]) >= 0
        
        res = []
        isNewAdded = False
        for i, interval in enumerate(intervals):
            start ,end  = interval [0], interval[1]
            
            if not isNewAdded:
                if doesIntervalsOverlap(interval, newInterval):
                    res.append([min(newInterval[0], start), max(newInterval[1], end)])
                    isNewAdded = True
            if len(res) == 0:
                res.append(interval)
            else:
                curr = res[-1]
                if doesIntervalsOverlap(interval, curr):
                    curr[0] = min(curr[0], start)
                    curr[1] = max(curr[1], end)
                else:
                    res.append(interval)
                    
            
        if not isNewAdded:
            res.append(newInterval)
            res.sort()
        return res
        
        