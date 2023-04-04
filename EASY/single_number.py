class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0 # n ^ 0 = n
        for i in nums:
            output = i ^ output
        
        return output
            