class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stairs_to_cheapest = {}
        # stairs_to_cheapest[i] is the cheapest way to get past stair at index i
        # return stairs_to_cheapest[i+1]
        #[2,1]
        stairs_to_cheapest[0] = 0
        stairs_to_cheapest[1] = 0

        for i in range(2, len(cost)+1):
            # in order to get past stair i, u can go to stair i-1 and take 2 steps, or stair i-1, take 1 step and pay the cost
            stairs_to_cheapest[i] = min(stairs_to_cheapest[i-2] + cost[i-2], stairs_to_cheapest[i-1] + cost[i-1]  )

        print(stairs_to_cheapest)
        return stairs_to_cheapest[ len(cost)] 