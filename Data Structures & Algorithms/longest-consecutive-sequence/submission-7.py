class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n= len(nums)
        nums =sorted(set(nums))
        longest = curr = 1

        if not nums:
            return 0
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]+1:
                curr +=1
            else:
                longest = max(longest, curr)
                curr =1
        return max(longest, curr)
            