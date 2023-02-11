class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = defaultdict(int)
        res, perm = [], []
        
        for n in nums:
            counts[n] += 1
        
        def backTrack():
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for n in counts:
                if counts[n] > 0:
                    perm.append(n)
                    counts[n] -= 1
                    
                    backTrack()
                    
                    counts[n] += 1
                    perm.pop()
        backTrack()
        return res