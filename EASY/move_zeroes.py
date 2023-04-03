class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # left, right = 0, 1

        # if len(nums) <= 1:
        #     return nums

        # while right < len(nums) -1:
        #     if nums[left] == 0 and nums[right] != 0:
        #         nums[left] = nums[right]
        #         nums[right] = 0
        #         left += 1
        #         right += 1
            
        #     elif nums[left] == 0 and nums[right] == 0:
        #         right += 1


        #     else:
        #         left += 1
        #         right += 1
        


        # return nums

        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums

            
                
