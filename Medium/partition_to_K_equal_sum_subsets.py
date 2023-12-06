from pytictoc import TicToc

t = TicToc()

class Solution:
    def canPartitionKSubsets(self, nums, k) -> bool:
        total_sum = sum(nums)
        
        # Check if total sum is divisible by k
        if total_sum % k:
            return False

        nums.sort(reverse=True)  # Sort in reverse order

        if nums[0] > total_sum // k:
            return False

        target = total_sum // k
        used = [False] * len(nums)

        memo = {}

        def backtrack(start, k, current_sum):
            if k == 0:  # Base case: k subsets formed
                return True
            if current_sum == target:  # Current subset formed, proceed to next subset
                return backtrack(0, k - 1, 0)
            
            if (start, tuple(used)) in memo:
                return memo[(start, tuple(used))]

            for i in range(start, len(nums)):
                # Skip duplicates
                if i > 0 and not used[i - 1] and nums[i] == nums[i - 1]:
                    continue
                if used[i] or current_sum + nums[i] > target:
                    continue
                used[i] = True
                if backtrack(i + 1, k, current_sum + nums[i]):
                    return True
                used[i] = False  # Backtrack

            return False

        return backtrack(0, k, 0)
    
# Example usage
t.tic()

nums = [9,6,1,8,4,3,4,1,7,3,7,4,5,3,2,3]
k = 4
solution = Solution()
print(solution.canPartitionKSubsets(nums, k))

t.toc()
