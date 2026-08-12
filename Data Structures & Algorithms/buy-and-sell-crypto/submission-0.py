class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_p =0
        for i in range(n):
            for j in range(i+1, n):
                if prices[i]<prices[j]:
                    profit = prices[j]-prices[i]
                    max_p = max(max_p, profit)
        return max_p