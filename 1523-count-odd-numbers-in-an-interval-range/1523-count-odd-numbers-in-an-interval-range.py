class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n = (high - low) // 2
        
        # if either high or low is odd
        if (high % 2 != 0 or low % 2 != 0):
            return n + 1
        return n
        