class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] is fewest number of coins to make i
        # return dp[amount]
        dp = {}
        if amount == 0:
            return 0
        dp[0] = 0
        for i in range(1,amount+1): #1
            dp[i] = float('inf')
            for coin in coins:
                remainder = i - coin
                if remainder >= 0:
                    cheapest_way_to_make_remainder = dp[remainder]
                    dp[i] = min(dp[i],cheapest_way_to_make_remainder + 1)
               
        print(dp)           
        if dp[amount] == float('inf'):
            return -1
        
        return dp[amount]

            


