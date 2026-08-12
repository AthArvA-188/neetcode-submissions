class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if not prices:
            return res
        # i = 0
        # j = i+1
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                cur = prices[j]- prices[i]
                if cur>res:
                    res = cur
        return res




