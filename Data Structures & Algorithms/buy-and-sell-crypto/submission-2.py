class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0

        buyI = 0
        sell = 0

        for i in range(len(prices) - 1):
            if prices[i+1] < prices[buyI]:
                buyI = i + 1
        
        for i in range(buyI + 1, len(prices) ):
            if i == len(prices) - 1:
                break
            sell = max(prices[i], prices[i+1])

        # maxProfit = max((sell - buy), maxProfit)
        if sell - prices[buyI] > maxProfit:
            maxProfit = sell - prices[buyI]

        return maxProfit
