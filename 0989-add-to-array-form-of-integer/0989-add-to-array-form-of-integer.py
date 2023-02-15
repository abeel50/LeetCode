class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        c = 0
        res = []
        while i >= 0 or k != 0:
            d = k % 10
            k = k // 10
            s = 0
            if i >= 0:
                s = num[i] + d + c
            else:
                s = d + c
            c = 0
            if s > 9:
                res.append(s %10)
                c = s // 10
            else:
                res.append(s)
            i -= 1
            
        if c > 0:
            res.append(c)
        
        
        return res[::-1]
            
        