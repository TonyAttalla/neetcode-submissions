class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # compute current value - target, that is what you need in order to achieve current_value + potential = target

        # [2,7,11,15]
        # [5,2,-2, -6]
        # compute a set of opposites and their index

        # iterate through list. compute what you need (target - curr), if that value is in opposites, return this index + its index
        
        numbers_to_indeces = {}
        for i in range(len(nums)):
            value = nums[i]
            numbers_to_indeces[value] = i
        # {1:0, 3:1, 4:2, 2:3 }

        for i in range(len(nums)):
            value = nums[i]
            if target-value in numbers_to_indeces:
                if numbers_to_indeces[target-value] != i:
                    return_val = []
                    return_val.append(numbers_to_indeces[target-value])
                    return_val.append(i)
                    return_val.sort()  
                    return return_val  
        