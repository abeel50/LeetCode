class Solution:
    def trimMean(self, arr: List[int]) -> float:
        l = len(arr)
        arr.sort()
        fivePercent = int(l * 0.05)
        l -= (fivePercent * 2)
        return sum(arr[fivePercent: len(arr)-fivePercent])/ l        