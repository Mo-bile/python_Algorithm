class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        
        n = len(prices)
        max_price = [0] * n
        max_profit = 0

        max_price[-1] = prices[-1]
        for i in range(n-2, -1, -1):
            max_price[i] = max(max_price[i+1], prices[i])

        print(max_price)
        # for m in range(n):
        #     max_price.append(max(prices[m:])) 
        
        for i in range(n):
            # profit.append(max_price[i] - prices[i])
            max_profit = max(max_price[i] - prices[i], max_profit)
        
        return max_profit
        