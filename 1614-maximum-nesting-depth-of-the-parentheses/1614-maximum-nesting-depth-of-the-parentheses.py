class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        curMax = 0
        
        for c in s:
            if c =="(":
                curMax += 1
            elif c== ")":
                curMax -= 1
            else:
                continue
            res = max(res, curMax)
        return res
