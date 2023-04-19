class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # base case
        if (len(nums) == 1):
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0)

            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)

            # add the element back
            nums.append(n)

        return result

        
