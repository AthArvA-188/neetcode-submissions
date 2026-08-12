class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        
        res =0
        i, j = 0, len(height)-1
        lm =rm = 0
        while i<j:
            if height[i]<height[j]:
                if lm<height[i]:
                    lm= height[i]
                else:
                    res +=lm-height[i]
                i+=1
            else:
                if rm<height[j]:
                    rm = height[j]
                else:
                    res+= rm-height[j]
                j-=1
        return res


        