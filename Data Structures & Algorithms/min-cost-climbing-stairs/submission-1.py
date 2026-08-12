class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)
        # dyp =[0]*(n+1)
        
        # for i in range(2, n+1):
        #     dyp[i] = min(dyp[i-1]+cost[i-1], dyp[i-2]+cost[i-2])

        # return dyp[n]
        for i in range(len(cost)-3, -1,-1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])