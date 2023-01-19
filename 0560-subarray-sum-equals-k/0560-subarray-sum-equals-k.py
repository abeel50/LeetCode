class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # to store count of subarrays
        res = 0
        # curr Sum
        curSum = 0
        #hash map of mods 
        prefixSum ={0:1}
        
        for n in nums:
            #compute curMode
            curSum += n
            diff = curSum - k
            
            # if sum exits in hashmap then it means it will create x subarrays as it's count
            res += prefixSum.get(diff, 0)
            # adding sum to hash
            prefixSum[curSum] = 1 + prefixSum.get(curSum,0)
            
        return res
        