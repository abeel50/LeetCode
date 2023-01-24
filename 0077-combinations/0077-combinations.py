class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res  = []
        
        def rec(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for i in range(start, n + 1):
                comb.append(i)
                rec(i + 1 , comb)
                comb.pop()
            
        rec(1, [])      
        return res
                
        