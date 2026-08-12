class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        p=0
        minPrice = float("inf")

        for price in prices:
            if price<minPrice:
                minPrice = price
            else:
                p = price- minPrice
                if p>maxprofit:
                    maxprofit = p
        return maxprofit

