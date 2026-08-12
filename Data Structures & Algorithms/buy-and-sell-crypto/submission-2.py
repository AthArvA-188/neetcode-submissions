class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro =0
        # min_p = float('inf')
        l,r= 0,1
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if prices[i]<prices[j]:
        #             profit = prices[j]-prices[i]
        #             max_p = max(max_p, profit)
        # return max_p
        # for price in prices:
        #     if price<min_p:
        #         min_p = price
        #     else:
        #         profit = price-min_p
        #         if profit>max_pro:
        #             max_pro = profit
        # return max_pro
        while r<len(prices):
            if prices[l]<prices[r]:
                pro = prices[r]-prices[l]
                max_pro = max(pro, max_pro)
            else:
                l= r
                
            r+=1
        return max_pro