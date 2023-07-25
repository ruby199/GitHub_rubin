from typing import List

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        # Initialize the result 'res' to store the maximum min-product sum.
        res = 0
        
        # Initialize a stack to store pairs (index, value) of elements in 'nums'.
        stack = []
        
        # Create a prefix sum array 'prefix' to quickly calculate the sum of elements up to a certain index.
        # The prefix sum helps in calculating the total sum of elements between two indices efficiently.
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)

        # Start iterating through the elements of 'nums' along with their indices.
        for i, n in enumerate(nums):
            newStart = i
            
            # While the stack is not empty and the top element's value is greater than the current element's value 'n',
            # pop elements from the stack and calculate the min-product sum for each popped element.
            while stack and stack[-1][1] > n:
                start, val = stack.pop()
                total = prefix[i] - prefix[start]
                res = max(res, val * total)
                newStart = start
            
            # Append the current element (index, value) pair to the stack.
            stack.append((newStart, n))

        # After the iteration, there might be some elements left in the stack.
        # Calculate the min-product sum for each of these remaining elements and update 'res'.
        for start, val in stack:
            total = prefix[len(nums)] - prefix[start]
            res = max(res, val * total)

        # Return the maximum min-product sum, modulated by 10^9 + 7










