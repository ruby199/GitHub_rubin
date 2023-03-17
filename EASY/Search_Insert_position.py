class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # do better than O(n) searching left to right
        # to log(n) by using "Binary Search"

        # Middle = (L+R)/2
        # check if the middle value is bigger/smaller than the curr

        left_index, right_index = 0, len(nums)-1
        
        while left_index <= right_index:
            middle_index = (left_index + right_index)//2

            if target == nums[middle_index]:
                return middle_index

            if target > nums[middle_index]:
                left_index = middle_index + 1
            else:
                right_index = middle_index -1
            
        # if never reach the target
        return left_index





