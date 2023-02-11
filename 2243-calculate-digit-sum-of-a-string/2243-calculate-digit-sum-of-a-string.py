class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        def rec(ss):
            # base case
            if len(ss) <= k: return ss
                    
            res, i= [], 0
            while i < len(ss):
                if (i + k) < len(ss):
                    res.append(str(sum([int(v) for v in ss[i: i + k]])))
                else:
                    res.append(str(sum([int(v) for v in ss[i:]])))
                i += k
            return rec("".join(res))
        return rec(s)
            

        
        