class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        nums1 = nums[:n-1]
        nums2 = nums[1:]
        print(nums1)
        # print(nums2)
        rob1, rob2 = 0,0
        for num in nums1:
            temp = max(num + rob1, rob2)
            rob1 =rob2
            rob2 = temp
        rob3, rob4 = 0,0 
        for num in nums2:
            temp = max(num + rob3, rob4)
            rob3 =rob4
            rob4 = temp
        return max(rob2, rob4)

        