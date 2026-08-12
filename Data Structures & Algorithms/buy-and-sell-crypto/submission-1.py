class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p =0
        min_p = float('inf')
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if prices[i]<prices[j]:
        #             profit = prices[j]-prices[i]
        #             max_p = max(max_p, profit)
        # return max_p
        for price in prices:
            if price<min_p:
                min_p = price
            else:
                profit = price-min_p
                if profit>max_p:
                    max_p = profit
        return max_p