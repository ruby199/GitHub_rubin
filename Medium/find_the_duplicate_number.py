class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # easy way is to use hash set, but we can only use constant extra spce.

        # linked list cycle problem & Floyd's algorithm

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow



