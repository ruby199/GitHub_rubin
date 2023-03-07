from ast import List


class Solution:
    def maxSubArray(nums):
        maxSubarray = nums[0]
        currentSum = 0

        for n in nums:
            if currentSum < 0:
                currentSum = 0 #reset back to zero, since we do not need negitive prefix
            currentSum += n
            maxSubarray = max(maxSubarray, currentSum)

        return maxSubarray


print(Solution.maxSubArray([1,2,3,-1,3,-5,8]))