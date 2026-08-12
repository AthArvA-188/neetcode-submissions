class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top = {}
        for num in nums:
            top[num] = 1+ top.get(num, 0)
        heap = []
        for num in top.keys():
            heapq.heappush(heap, (top[num], num))
            if len(heap)>k:
                heapq.heappop(heap)
        res =[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
                
