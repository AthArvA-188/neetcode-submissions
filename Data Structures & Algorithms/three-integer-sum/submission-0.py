class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target =0
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k]==target and [nums[i], nums[j], nums[k]] not in ans:
                        ans.append([nums[i], nums[j],nums[k]])
        return ans