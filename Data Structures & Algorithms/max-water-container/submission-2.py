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
        mvol = cvol =0
        while l<r:
            height = min(heights[l], heights[r])
            cvol = height * (r-l)
            if cvol>mvol:
                mvol = cvol
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return mvol