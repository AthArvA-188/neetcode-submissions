class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxvol = 0
        i, j = 0, len(heights)-1
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):

                cvol = min(heights[i], heights[j])*(j-i)

                maxvol = max(cvol, maxvol)
        return maxvol
        