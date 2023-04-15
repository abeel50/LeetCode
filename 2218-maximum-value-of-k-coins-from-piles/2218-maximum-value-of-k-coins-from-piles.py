class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        # for dp caching
        dp = [[-1] * (k+1) for _ in range(n)]
        
        def dfs(i, coins):
            #Base case if piles are done
            if i == n:
                return 0
            
            # check if already computed in cache
            if dp[i][coins] != -1:
                return dp[i][coins]
            
            dp[i][coins] = dfs(i+1, coins)
            
            curPile = 0
            for j in range(min(coins, len(piles[i]))):
                curPile += piles[i][j]
                dp[i][coins] = max(dp[i][coins], curPile + dfs(i + 1, coins - j - 1))
            return dp[i][coins]
        
        return dfs(0, k)
        