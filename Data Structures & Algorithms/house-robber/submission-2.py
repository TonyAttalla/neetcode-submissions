class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] represents the max profit robbing up to (and including) house i
        dp = {}
        if len(nums) == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i, profit in enumerate(nums):
            if i<=1:
                continue
            # choose to either rob or not rob
            # rob
            profit_with_robbing = dp[i-2] + nums[i]
            profit_no_robbing = dp[i-1]
            dp[i] = max(profit_with_robbing, profit_no_robbing)

        return dp[len(nums)-1]
        