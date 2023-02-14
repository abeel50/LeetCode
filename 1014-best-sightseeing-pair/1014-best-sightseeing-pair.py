class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # values[i] + i
        maxi = values[0] + 0
        res = -1
        
        for i in range(1, len(values)):
            #(values[i] + i) + values[j] - j
            # maxi + values[j] - j
            res = max(res, maxi + values[i] - i)
            maxi = max(maxi, values[i] + i)
        return res 