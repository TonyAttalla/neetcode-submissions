class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combinations = []

        # considers all numbers starting from index i
        def backtrack(i,curr_sum):
            # we've considered all nu
            if curr_sum > target or i>=len(nums):
                return
            elif curr_sum == target:
                res.append(combinations[:])
                return
            combinations.append(nums[i])
            backtrack(i,curr_sum + nums[i])
            combinations.pop()
            backtrack(i+1,curr_sum)
        backtrack(0,0)
        return res

 
        