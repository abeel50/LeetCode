class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0
        min_buy = float('inf')
        for price in prices:
            min_buy = min(min_buy, price)
            max_profit = max(max_profit, price-min_buy)
        return max_profit
                
        
        