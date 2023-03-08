class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hoursTakenToEat(n):
            return sum([math.ceil(p / n) for p in piles])
                    
        left, right = 1, max(piles)
        res = right
        
        while left <= right:
            k = (left + right) // 2
            hours = hoursTakenToEat(k)
            if hours <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1
                
        return res
        