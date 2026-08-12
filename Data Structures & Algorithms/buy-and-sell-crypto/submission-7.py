class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        tp =0 
        for sell in prices:
            if sell<minP:
                minP = sell
            tp= max(sell-minP, tp)
        return tp
