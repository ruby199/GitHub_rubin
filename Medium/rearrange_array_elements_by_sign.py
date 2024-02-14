"""
Problem Link: https://leetcode.com/problems/rearrange-array-elements-by-sign/description/?envType=daily-question&envId=2024-02-14


Description:

    You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
    You should rearrange the elements of nums such that the modified array follows the given conditions:

    [1] Every consecutive pair of integers have opposite signs. e.g., pos -> neg -> pos
    [2] For all integers with the same sign, the order in which they were present in nums is preserved. e.g., if pos1, pos2 -> the order remains same as pos1, pos2
    [3] The rearranged array begins with a positive integer. 
    [4] Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

Key Takeaways for rearrangeArray_1:

    [1] sort the array where the order among similar sign integers is preserved -> stable sorting for pos and neg separately
        * [DEF] stable sorting: if two elements have the same key, the one that appeared earlier in the input will also appear in the sorted output. 
    [2] We should alternate the elements by sign starting with pos num.

Key Takeaways for rearrangeArray_2:

    [1] Use two pointers to track even and odd indices
    [2] Iteratively fill the new array ans which has the same size as num

Both solution have the same time & space complexity:
    Time Complexity: O(n)
    Space Complexity: O(n)

"""


class Solution:
    def rearrangeArray_1(self, nums):
        # Runtime: Beats 97.89% of users with Python3
        # Memory: Beats 48.57% of users with Python3
        # Separate positive and negative numbers
        positives = [i for i in nums if i > 0]
        negatives = [i for i in nums if i < 0]

        result = []

        # Merge positive and negative numbers in alternating order, starting with pos
        for pos, neg in zip(positives, negatives):
            result.append(pos)
            result.append(neg)
        return result

    def rearrangeArray_2(self, nums): # Two pointers approach
        # Runtime: Beats 68.76% of users with Python3
        # Memory: Beats 69.94% of users with Python3

        if len(nums) <= 2:
            if nums[0] > 0 or (nums[0] < 0 and nums[1] < 0):
                return nums
            else:
                nums.reverse()
                return nums
        
        ans = [0] * len(nums)
        pos_pt = 0
        neg_pt = 1

        while neg_pt < len(nums) - 1 and pos_pt < len(nums) - 1:
            for num in nums:
                if num > 0:
                    ans[pos_pt] = num
                    pos_pt += 2
                
                if num < 0:
                    ans[neg_pt] = num
                    neg_pt += 2
            
        return ans
            


    def rearrangeArray_2_fixed(self, nums): # Two pointers approach modified
        # Runtime: Beats 89.67% of users with Python3
        # Memory: Beats 65.62% of users with Python3
        ans = [0] * len(nums)
        pos_pt, neg_pt = 0, 1  # Start pointers for positive and negative numbers
        
        for num in nums:
            if num > 0:
                ans[pos_pt] = num
                pos_pt += 2
            else:
                ans[neg_pt] = num
                neg_pt += 2
        
        return ans
        










nums = [3, 1,-2,-5,2,-4]
# nums = [-1, 1]

sol = Solution()
print(sol.rearrangeArray_1(nums))
print(sol.rearrangeArray_2_fixed(nums))



