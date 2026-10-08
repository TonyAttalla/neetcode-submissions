class Solution:
    def climbStairs(self, n: int) -> int:
        # number of ways to get to stair n = number of ways to get to stair n-1 + number of ways to get to stair n-2
        dp = [0] * n
        if n >=2:
            dp[0] = 1
            dp[1] = 2
        # dp[i]  = num ways to get to stair i
        if n == 1:
            return 1
        
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]
        