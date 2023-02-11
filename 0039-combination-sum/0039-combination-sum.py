class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, comb, total):
            if total == target:
                res.append(comb[:])
                return
            
            if i >= len(candidates) or total > target:
                return
            
            #including current number
            comb.append(candidates[i])
            dfs(i, comb, total + candidates[i])
            
            #withour including current number
            comb.pop()
            dfs(i + 1, comb, total)
            
        dfs(0, [], 0)
        return res