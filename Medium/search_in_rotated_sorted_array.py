class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # binary search
        while l<= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            # are we in the left sorted portion? check:
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1 # go to right portion
            # right sorted portion?
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1