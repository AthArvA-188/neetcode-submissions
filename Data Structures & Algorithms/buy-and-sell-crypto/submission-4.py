class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       max_p=0
       min_p= float("inf") 
       profit = 0
       for price in prices:
        if price<min_p:
            min_p = price
        else:   
            profit = price-min_p
            if profit>max_p:
                max_p = profit
       return max_p

