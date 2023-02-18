class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        h = defaultdict(int)
        for n in nums:
            h[n] += 1
        
        pairs, alone = 0, 0
        for v in h.values():
            if v % 2 != 0:
                alone += 1    
            pairs += v // 2
            
        return [pairs, alone]
                
            
            
        