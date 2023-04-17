class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mxCandy = max(candies)
        return [True if c + extraCandies >= mxCandy else False for c in candies]
        