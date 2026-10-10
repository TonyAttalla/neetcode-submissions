class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] -> # of ways to get to coord i,j from the top left
        # dp[i][j] = look at above cell and left cell

        dp = {}
        dp[(0,0)] = 1
        
        for i in range(m):
            for j in range(n):
                if (i,j) not in dp:
                     dp[(i,j)] = 0
                if (i-1,j) in dp: 
                    dp[(i,j)] += dp[i-1,j]
                if (i,j-1) in dp:
                    dp[(i,j)] += dp[i,j-1] 
        
        return dp[(m-1,n-1)]
        