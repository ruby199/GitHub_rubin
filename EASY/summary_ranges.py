"""
Problem Link: https://leetcode.com/problems/summary-ranges/?envType=study-plan-v2&envId=top-interview-150

"""

class Solution:
    def summaryRanges(self, nums):
        
        result = []
        i = 0

        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
            if start != nums[i]:
                result.append(str(start) + "->" + str(nums[i]))
            else:
                result.append(str(nums[i]))
            
            i += 1

        return result



            




sol = Solution()
nums = [0,2,3,4,6,8,9] # ["0","2->4","6","8->9"]
print(sol.summaryRanges(nums))