class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] # returned result
        nums.sort() # sort the array O(nlogn)

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: # not the first value & if same value as before
                continue # skip!
            
            l, r = i + 1, len(nums) - 1 # use the two pointer solution for the remaining portion of the array
            while l < r:
                threeSum = a + nums[l] + nums[r] # compute the sum
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]]) # is equal to 0
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1 # update left pointer once again if its same sum
        return res
