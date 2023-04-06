class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = n
        count = 0
        i = 0

        while left >= i+1:
            i += 1
            left -= i
            count += 1
        
        return count