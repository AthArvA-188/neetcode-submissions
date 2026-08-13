class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        res = r
        l = 1
        
        while l<=r:
            mid = (r+l)//2    
            time = 0
            for pile in piles:
                time += math.ceil(float(pile)/mid)
                
            if time>h:
                l =mid+1
            else:
                res = mid
                r = mid-1
        return res
                
        