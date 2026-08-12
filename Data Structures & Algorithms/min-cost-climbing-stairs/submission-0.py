class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one, two = cost[n-2], cost[n-1]
        dyp =[0]*(n+1)
        
        for i in range(2, n+1):
            dyp[i] = min(dyp[i-1]+cost[i-1], dyp[i-2]+cost[i-2])

        return dyp[n]