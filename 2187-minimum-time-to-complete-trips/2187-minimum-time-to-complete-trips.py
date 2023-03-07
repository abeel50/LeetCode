class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        if len(time) == 1: return totalTrips * time[0]
        l, r = 1, totalTrips * min(time)
        while l < r:
            tripCount = []
            mid = l + ( r - l)//2
            for i in time:
                tripCount.append(mid//i)
            s = sum(tripCount)
            if s < totalTrips:
                l = mid + 1
            else: r = mid
        return l