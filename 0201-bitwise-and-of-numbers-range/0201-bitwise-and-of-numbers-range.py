class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        return self.rangeBitwiseAnd(left >> 1, right >> 1) << 1 if left < right else left

        