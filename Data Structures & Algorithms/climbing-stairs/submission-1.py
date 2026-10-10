class Solution:
    def climbStairs(self, n: int) -> int:
        # identify subproblems
        # key insight
        # of ways to get to stair n = # of ways to get to stair n-1 + 1 =  n = # of ways to get to stair n-2 + 2
        dp = {} # maps step i to # of ways to get to step i

        for i in range(0,n):
           
            if i == 0:
                dp[i] = 1
            elif i == 1 :
                dp[i] = 2
            else:
                dp[i] = dp[i-2] + dp[i-1]
        print(dp)
        return dp[n-1]
        