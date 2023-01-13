class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3: return False

        N = len(arr)
        i = 0

        # walk up
        while i+1 < N and arr[i] < arr[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and arr[i] > arr[i+1]:
            i += 1

        return i == N-1
        