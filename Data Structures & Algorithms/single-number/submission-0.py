class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ct ={}
        for i in nums:
            ct[i] = ct.get(i, 0)+1

        for num in ct:
            if ct[num]==1:
                return num