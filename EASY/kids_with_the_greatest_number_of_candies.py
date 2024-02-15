"""
Problem Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

"""


class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        # Time Complexity: O(n) * O(n) = O(n^2) due to max operation
        # Memory Complexity: O(n) because of the result list
        result = []
        for i in range(len(candies)):
            prev_value = candies[i]
            new_amount = candies[i] + extraCandies
            candies[i] = new_amount

            if candies[i] == max(candies): # max function called inside the loop: O(n) per loop
                result.append(True)
            else:
                result.append(False)

            # print("cur list: ", str(candies))
            # print("max: ", str(max(candies)))
            # print(result[i])
            candies[i] = prev_value
        return result
        
    def kidsWithCandies_improved(self, candies, extraCandies):
        # Time Complexity: O(n) + O(n) = O(n)
        # Memory Complexity: O(n)
        maxCandies = max(candies)
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= maxCandies)
        return result


sol = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
# print(sol.kidsWithCandies(candies, extraCandies))
print(sol.kidsWithCandies_improved(candies, extraCandies))