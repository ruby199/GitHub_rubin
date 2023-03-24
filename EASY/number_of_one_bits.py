class Solution:
    def hammingWeight(self, n: int) -> int:
        # O(32) == O(1) constant time complexity
        # downside: we need to count every bits even if it's not 1

        res = 0
        # while n:
        #     res += n % 2
        #     n = n >> 1
        # return res

        while n:
            n &= (n - 1)
            res += 1
        return res


