class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_exists = {}
        for i, elem in enumerate(nums):
            nums_to_exists[elem] = i
        
        for j, elem in enumerate(nums):
            opposite = target - elem 
            if opposite in nums_to_exists and nums_to_exists[opposite] != j:

                ret_val = [nums_to_exists[opposite], j]
                ret_val.sort()
                return ret_val
            




        