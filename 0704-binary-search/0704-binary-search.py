class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(array, x, low, high):

            if high >= low:

                mid = low + (high - low)//2

                # If found at mid, then return it
                if array[mid] == x:
                    return mid

                # Search the left half
                elif array[mid] > x:
                    return binarySearch(array, x, low, mid-1)

                # Search the right half
                else:
                    return binarySearch(array, x, mid + 1, high)

            else:
                return -1
        return binarySearch(nums,target,0,len(nums)-1)
        