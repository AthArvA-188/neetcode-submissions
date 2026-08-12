class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_vol =0
        # for i in range(len(heights)-1):
        #     for j in range(i+1, len(heights)):
                
        #         min_length = min(heights[i], heights[j])
        #         dist = j-i
        #         vol = min_length * dist
        #         max_vol = max(max_vol, vol)

        # return max_vol

        l, r = 0, len(heights)-1
        max_vol =0

        while l<r:
            curr = min(heights[l], heights[r])*(r-l)
            max_vol = max(curr, max_vol)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max_vol