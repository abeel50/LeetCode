class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [j for j in range(l2 + 1)]
        
        for i in range(1, l1 + 1):
            newDp = [i] + [0] * l2
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    newDp[j] = dp[j - 1]
                else:
                    newDp[j] = min(newDp[j - 1], dp[j]) + 1
            dp = newDp

        return dp[l2]
                
        