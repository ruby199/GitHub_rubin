"""
Problem Link: https://leetcode.com/problems/n-th-tribonacci-number/description/

Dynamic Programming Approach.

- Time Complexity: O(n) due to loop inside the feb function,
- Space Complexity: O(n) due to arr trib[n]

"""

class Solution:
    def tribonacci(self, n: int) -> int:
        def feb(trib, n):
            for i in range(3, n + 1): 
                trib[i] = trib[i - 1] + trib[i - 2] + trib[i - 3]
            #     print(f"trib: {trib}, trib[i]: {trib[i]}")
            # print(f"final trib[n]: {trib[n]}")
            return trib[n]
        
        # Base case: 
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        

        # dp memoization
        trib = [0] * (n + 1)

        # # predefine the first three Tribonacci numbers : [0, 1, 1]
        trib[1], trib[2] = 1, 1

        # compute and return the n-th Tribonacci number using the inner function feb (pass in: trib, n)
        return feb(trib, n)



sol = Solution()

# Example usage
n1 = 4
n2 = 25
print(f"Tribonacci({n1}) = {sol.tribonacci(n1)}")
# print(f"Tribonacci({n2}) = {sol.tribonacci(n2)}")