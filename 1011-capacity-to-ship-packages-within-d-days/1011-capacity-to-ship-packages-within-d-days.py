class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
        
        def canShip(cap):
            ships, curCap = 1, cap
            for w in weights:
                # if weight is exceeding capcity of ship
                if curCap - w < 0:
                    ships += 1 #increase the ships
                    curCap = cap
                curCap -= w
            return ships <= days
                
        #not a typical Binary Search
        while l<= r:
            cap = (l + r) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res
            