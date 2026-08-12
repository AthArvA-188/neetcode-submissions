class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx ={}
        for i, num in enumerate(nums):
            complement = target -num

            if complement in idx:
                return [idx[complement], i]

            idx[num]= i
        return []