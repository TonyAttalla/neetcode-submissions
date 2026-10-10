class Solution:
    def search(self, nums: List[int], target: int) -> int:
                # check midpoint index (bottom_index + top_index // 2 )
        # floor divison btw //
        # if mid > target:
            # top = mid
            # go again
        # elif mid < target:
            # bottom = mid
            # go again
        # elif mid == target:
            # return mid
        #  [-1,0,2,4,6,8], target = 4
        # bottom = 0, top = 5  

        # mid_index = 2, nums[mid_index] = 2  
        # bottom_index = 2, top = 5

        # mid_index = 3, nums[mid_index] = 4
        # bottom_index=2 top_index = 3

        # mid_index = 3
        bottom_index = 0
        top_index = len(nums) - 1
        while bottom_index <= top_index:
            mid_index = (bottom_index + top_index) // 2
            if nums[mid_index] > target:
                top_index = mid_index-1
            elif nums[mid_index] < target:
                bottom_index = mid_index+1
            elif nums[mid_index] == target:
                return mid_index

        # if nums[bottom_index] == target:
        #     return bottom_index
        return -1
        
        