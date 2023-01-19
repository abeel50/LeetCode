class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # to store count of subarrays
        res = 0
        # currMod 
        curMod = 0
        #hash map of mods 
        prefixMod ={0:1}
        
        for n in nums:
            #compute curMode
            curMod = (curMod + n) % k
            # if mod exits in hashmap then it means it will create x subarrays as it's count
            res += prefixMod.get(curMod, 0)
            # adding mod to hash
            prefixMod[curMod] = 1 + prefixMod.get(curMod,0)
            
        return res
            
        
        