class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob_so_far[i] represents the amount of money u can get from robbing up to house i
        rob_so_far = {}
        if len(nums) == 1:
            return nums[0]
        if len(nums) <= 2:
            return max(nums[0], nums[1])
        rob_so_far[0] = nums[0]
        rob_so_far[1] = max(nums[0], nums[1])
        for i,val in enumerate(nums):
            # rob the house or dont
            if i>=2:
                rob_so_far[i] = max(rob_so_far[i-2] + val, rob_so_far[i-1])
        return rob_so_far[len(nums)-1]

        