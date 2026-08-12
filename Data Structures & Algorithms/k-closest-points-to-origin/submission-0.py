class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist =[]
        


        for x,y in points:
            dist_org = (x**2+y**2)
            dist.append([dist_org, x, y])
        
        heapq.heapify(dist)
        res =[]
        while k>0:
            dist_org, x, y =heapq.heappop(dist)
            res.append([x,y])
            k-=1
        return res
