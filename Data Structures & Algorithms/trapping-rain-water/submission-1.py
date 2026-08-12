class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        # n = len(height)
        # l, r = 0, n
        # max_vol = 0
        # for i in range(n):
        #     leftmax= rightmax = height[i]

        #     for j in range(i):
        #         leftmax = max(leftmax, height[j])
            
        #     for j in range(i+1, n):
        #         rightmax = max(rightmax, height[j])

        #     max_vol += min(leftmax,rightmax) - height[i]

        # return max_vol

        l, r = 0 , len(height)-1
        leftmax, rightmax = height[l], height[r]
        res =0
        while l<r:
            if leftmax<rightmax:
                l+=1
                leftmax = max(leftmax, height[l])
                res +=leftmax-height[l]
                
            else:
                r-=1
                rightmax = max(rightmax, height[r])
                res +=rightmax-height[r]
            
                
        return res
            
