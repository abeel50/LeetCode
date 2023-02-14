class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos, neg, res = 0, 0, 0
        
        for n in nums:
            if n > 0:
                pos += 1
                neg = neg + 1 if neg else 0
            elif n < 0:
                temp = pos
                pos = 1 + neg if neg else 0
                neg = 1 + temp
            else:
                pos, neg = 0, 0
            res = max(pos, res)
            
        return res