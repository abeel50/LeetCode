class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def dfs(pos, comb, total):
            if total == 0:
                res.append(comb[:])
            
            if total <= 0:
                return
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                comb.append(candidates[i])
                dfs(i + 1, comb, total - candidates[i])
                comb.pop()
                prev = candidates[i]
            
        dfs(0, [], target)
        return res
        