class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        n = len(arr)
        new_arr = [0] * (arr[-1] + k + 1)
        for x in arr:
            if x > 0:
                new_arr[x] = 1
        count = 0
        for i in range(1, arr[-1] + k + 1):
            if new_arr[i] == 0:
                count += 1
                if count == k:
                    return i
            
        