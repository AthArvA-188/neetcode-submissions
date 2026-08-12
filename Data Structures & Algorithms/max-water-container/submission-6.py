class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i =0
        j = len(heights) -1
        while i<j:
            if heights[i]<heights[j]:
                mini = heights[i]
            else:
                mini = heights[j]
            cur_res = mini*(j-i)
            res = max(res, cur_res)

            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return res