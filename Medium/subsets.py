class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i): # i is the index of the value we are making decision on. 
            if i >= len(nums): # i happens to be out of bound
                res.append(subset.copy()) # set is going to be modified in python
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0) # first value

        return res
