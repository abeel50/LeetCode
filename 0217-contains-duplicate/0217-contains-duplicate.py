class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = defaultdict(int)
        nums.sort()
        
        for n in nums:
            h[n] +=1
            if h[n] > 1:
                return True
        return False
        