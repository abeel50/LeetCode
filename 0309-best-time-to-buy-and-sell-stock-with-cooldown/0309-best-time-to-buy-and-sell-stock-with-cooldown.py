class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #key = (i:index, buying:boolean), val = maxProfit
        dp = {}
        
        def rec(i, buying):
            if i >= len(prices): return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = rec(i + 1, buying)
            
            #if buy --> i + 1
            if buying:
                buy = rec(i + 1, not buying)- prices[i]
                dp[(i, buying)] = max(buy, cooldown)
                
            #if sell --> i + 2 e.g. you sell your stock, 
            # you cannot buy stock on the next day
            else:
                sell = rec(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]
        return rec(0, True)