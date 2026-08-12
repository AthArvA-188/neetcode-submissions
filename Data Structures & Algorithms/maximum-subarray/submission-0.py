class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msum = csum = nums[0]

        for n in nums[1:]:
            csum = max(n, csum  +  n)
            msum = max(msum, csum)
        return msum