class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(array, x, low, high):

            if high >= low:

                mid = low + (high - low)//2

                # If found at mid, then return it
                if array[mid] == x:
                    return True

                # Search the left half
                elif array[mid] > x:
                    return binarySearch(array, x, low, mid-1)

                # Search the right half
                else:
                    return binarySearch(array, x, mid + 1, high)

            else:
                return False
        
        
        low ,high = 0, len(matrix)-1
        while low <= high:
            mid = (low + high ) // 2
            curr = matrix[mid]
            if target >= curr[0] and target <= curr[-1]:
                return binarySearch(curr,target,0,len(curr)-1 )
            elif target < curr[0]:
                high = mid -1
            else:
                low = mid + 1
        return False
            