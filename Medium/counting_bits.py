class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1) # initialized to 0
        ans = [0] # n is going to be at least 0
        offset = 1 # highest power of 2

        for i in range(1, n + 1):
            if offset * 2 == i: # current end we just reached
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp
