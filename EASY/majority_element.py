class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # # sol1 HashMap  
        # count = {} # occurence of the each value
        # res, maxCount = 0, 0

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        #     res = n if count[n] > maxCount else res
        #     maxCount = max(count[n], maxCount)
        
        # return res
                

        # sol2 Boyer-Moore Alg

        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res

