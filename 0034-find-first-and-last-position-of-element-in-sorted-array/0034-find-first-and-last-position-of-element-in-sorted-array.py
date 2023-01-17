class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        res =[-1, -1]
        def binarySearch(array, x, low, high):

            if high >= low:

                mid = low + (high - low)//2

                # If found at mid, then return it
                if array[mid] == x:
                    res[0] = mid
                    res[1] = mid
                    mid += 1
                    while mid < len(nums) and array[mid] == x:
                        res[1] = mid
                        mid += 1
                    mid = res[0]
                    mid -= 1
                    while mid >= 0  and array[mid] == x:
                        res[0] = mid
                        mid -= 1
                    res.sort()

                # Search the left half
                elif array[mid] > x:
                    return binarySearch(array, x, low, mid-1)

                # Search the right half
                else:
                    return binarySearch(array, x, mid + 1, high)

            else:
                return 
        binarySearch(nums,target,0,len(nums)-1)
        return res
        