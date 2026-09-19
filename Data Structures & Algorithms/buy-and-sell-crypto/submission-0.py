class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMin = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < currentMin:
                currentMin = prices[i]
            newProfit = prices[i] - currentMin
            if newProfit > profit:
                profit = newProfit
        return profit
