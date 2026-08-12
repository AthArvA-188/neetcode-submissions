class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # target =0
        # nums = sorted(nums)
        # ans = []
        # for i in range(len(nums)-2):
        #     for j in range(i+1,len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i]+nums[j]+nums[k]==target and [nums[i], nums[j], nums[k]] not in ans:
        #                 ans.append([nums[i], nums[j],nums[k]])
        # return ans
        nums.sort()
        ans =[]
        n = len(nums)

        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left, right = i+1, n-1
            while left<right:
                total = nums[i]+nums[left] + nums[right]
                if total <0:
                    left+=1
                elif total >0:
                    right-=1
                else:
                    ans.append([nums[i], nums[left], nums[right]])

                    while left <right and nums[left]==nums[left+1]:
                        left+=1
                    while left < right and nums[right]==nums[right-1]:
                        right-=1
                    right-=1
                    
        return ans