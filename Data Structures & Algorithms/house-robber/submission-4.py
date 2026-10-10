class Solution:
    def rob(self, nums: List[int]) -> int:
        # cant rob nums[0] and nums[-1]
        # dp[i] represents max profit of robbing nums[0] through
        # nums[i]
        if len(nums) < 2:
            return nums[0]
        dp = {}
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for i in range(2,len(nums)):
            # rob or not rob
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[len(nums)-1]